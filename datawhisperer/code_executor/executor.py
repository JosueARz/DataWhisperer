# Copyright 2024 JosueARz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import ast
import io
import re
import sys
from typing import Any, Dict, Optional, Tuple

import pandas as pd
import plotly.graph_objects as go

from datawhisperer.code_executor.fixer import CodeFixer


def sanitize_code(code: str) -> str:
    """
    Cleans LLM-generated code by removing Markdown formatting and disallowed calls.

    Args:
        code (str): Raw code string from the LLM.

    Returns:
        str: Cleaned Python code.
    """
    code = code.strip()

    # Remove triple backticks and optional "python" prefix
    if code.startswith("```"):
        code = code.strip("`").strip()
        if code.startswith("python"):
            code = code[6:].strip()

    # Remove any fig.show() or plt.show() calls
    code = re.sub(r"^\s*(fig|plt)\.show\s*\(\s*\)\s*;?\s*$", "", code, flags=re.MULTILINE)
    code = code.replace("fig.show()", "")

    return code.strip()


def detect_last_of_type(context: Dict[str, Any], expected_type: type, exclude: str = "df") -> Any:
    """
    Returns the last object of a specific type in the context, excluding a given name.
    """
    for key in reversed(list(context.keys())):
        if key != exclude and isinstance(context[key], expected_type):
            return context[key]
    return None


def detect_last_dataframe(
    context: Dict[str, Any],
    dataframe_name: str,
    generated_names: Optional[list[str]] = None,
) -> Optional[pd.DataFrame]:
    """
    Detects the last generated DataFrame (different from the original).

    If `generated_names` is provided, uses it to find the most recent valid DataFrame.
    """
    original_df = context.get(dataframe_name)

    if generated_names:
        for name in reversed(generated_names):
            candidate = context.get(name)
            if isinstance(candidate, pd.DataFrame) and candidate is not original_df:
                return candidate

    for key in reversed(list(context.keys())):
        val = context[key]
        if isinstance(val, pd.DataFrame) and val is not original_df:
            return val

    return None



def detect_last_plotly_chart(context: Dict[str, Any]) -> Any:
    """
    Detects the last Plotly object in the execution context.
    """
    for key in reversed(list(context.keys())):
        val = context[key]
        if hasattr(val, "to_plotly_json"):
            return val
    return None


def run_user_code(
    code: str, context: Dict[str, object], dataframe_name: str
) -> Tuple[str, Any, Any, str, bool]:
    """
    Executes user-generated code in a controlled context.

    Returns:
        (output_text, table_result, chart_result, final_code, success_flag)
    """
    code = sanitize_code(code)
    stdout = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = stdout

    table_result = None
    chart_result = None
    output_text = ""

    try:
        parsed = ast.parse(code, mode="exec")
        last_expr = parsed.body[-1] if isinstance(parsed.body[-1], ast.Expr) else None
        if last_expr:
            parsed.body = parsed.body[:-1]

        local_context = context.copy()
        before_keys = set(local_context.keys())

        exec(compile(ast.Module(parsed.body, type_ignores=[]), "<exec>", "exec"), local_context)

        # Detectar nuevos DataFrames
        after_keys = set(local_context.keys())
        new_vars = list(after_keys - before_keys)
        generated_dataframes = [var for var in new_vars if isinstance(local_context[var], pd.DataFrame)]


        final_value = None
        if last_expr:
            final_value = eval(compile(ast.Expression(last_expr.value), "<eval>", "eval"), local_context)

        output_text = context.get("Respuesta") or stdout.getvalue().strip()

        table_result = detect_last_dataframe(local_context, dataframe_name, generated_dataframes)
        
        if table_result is None and isinstance(final_value, pd.DataFrame):
            table_result = final_value

        chart_result = detect_last_plotly_chart(context)
        if chart_result is None and hasattr(final_value, "to_plotly_json"):
            chart_result = final_value

        return output_text.strip(), table_result, chart_result, code, True

    except ModuleNotFoundError as e:
        missing_module = str(e).split("'")[1]  # extrae 'XXX' de "No module named 'XXX'"
        message = f"Para responder esta pregunta, necesitas instalar la librería `{missing_module}`."
        return message, None, None, code, False

    except Exception as e:
        return f"Execution error:\n{e}", None, None, code, False


    finally:
        sys.stdout = sys_stdout


def run_with_repair(
    code: str,
    question: str,
    context: Dict[str, object],
    schema: Dict[str, str],
    dataframe_name: str,
    api_key: str,
    model: str,
) -> Tuple[str, Any, Any, str, bool]:
    """
    Executes code generated by an LLM. If execution fails, attempts automatic repair via LLM.

    Returns:
        (final_text, final_table, final_chart, final_code, success_flag)
    """
    code_clean = sanitize_code(code)
    text, table, chart, final_code, success = run_user_code(code_clean, context, dataframe_name)

    if success:
        return text, table, chart, final_code, True

    fixer = CodeFixer(api_key, model)
    repaired_code = fixer.fix_code(question, code_clean, text, schema, dataframe_name)

    repaired_text, repaired_table, repaired_chart, _, repaired_success = run_user_code(
        repaired_code, context, dataframe_name
    )

    return repaired_text, repaired_table, repaired_chart, repaired_code, repaired_success
