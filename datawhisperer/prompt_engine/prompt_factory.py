# Copyright 2024 JosueARz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""System prompt generator, built by OpenAI model based on the provided schema."""

from typing import Dict

from datawhisperer.llm_client.openai_client import OpenAIClient


class PromptFactory:
    """
    Uses the OpenAI model to dynamically generate a 'system' message
    instructing it to behave as a Python code generator for a given DataFrame.
    """

    def __init__(
        self,
        api_key: str,
        model: str,
        dataframe_name: str,
        schema: Dict[str, str],
        client=None,  # ✅ nuevo parámetro opcional
    ) -> None:
        """
        Initializes the factory with a connection to the OpenAI client.

        Args:
            api_key (str): OpenAI API key.
            model (str): OpenAI model to use (e.g., gpt-4).
            dataframe_name (str): Name of the DataFrame in user code.
            schema (Dict[str, str]): Dictionary with column names and descriptions.
        """
        self.dataframe_name = dataframe_name
        self.schema = schema
        self.client = client or OpenAIClient(api_key, model)

    def build_system_prompt(self) -> str:
        """
        Uses the OpenAI model to build the ideal system message based on the schema.

        Returns:
            str: Content for the 'system' role.
        """
        schema_description = "\n".join(f"- `{col}`: {desc}" for col, desc in self.schema.items())

        instruction = f"""
        You are a Python code generator that answers questions about a DataFrame named `{self.dataframe_name}`.
        Use only `pandas` for data manipulation and `plotly` for data visualization.

        Strict rules:
        - Never create dummy data or use pandas.read_csv, read_excel, or any external sources.
        - The code must be **complete, functional, and runnable without any additional context**.
        - Always include the necessary `import` statements at the top.
        - Always iclude the import of libraries.
        - Do not use `matplotlib`, `seaborn`, or any `plt.show()` calls.
        - If using Plotly, **do NOT include `fig.show()`** — assume the environment (like Jupyter) will display it.
        - If the question requires multiple DataFrames or preprocessing steps:
            - First generate all necessary steps to construct a **single final output DataFrame**.
            - Then, based on that final DataFrame, answer the question.
        - Always use `print()` if the answer involves a specific value (count, summary, etc.).
        - Do not split the output into blocks or show intermediate results.
        - The code must produce **a single final output** — either a printed value or a plot.
        - Never explain anything. Only return Python code.

        Column reference and descriptions:
        {schema_description}
        """

        return instruction.strip()
