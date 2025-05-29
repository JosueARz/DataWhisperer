# Copyright 2024 JosueARz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from typing import Dict

from datawhisperer.llm_client.gemini_client import GeminiClient
from datawhisperer.llm_client.openai_client import OpenAIClient


class CodeFixer:
    """
    Uses an LLM (OpenAI or Gemini) to fix Python code that failed to execute,
    based on the error message and schema.
    """

    def __init__(self, api_key: str, model: str = "gpt-4.1-mini"):
        if model.startswith("gemini"):
            self.client = GeminiClient(api_key=api_key, model_name=model)
        else:
            self.client = OpenAIClient(api_key=api_key, model=model)

    def fix_code(
        self, question: str, code: str, error: str, schema: Dict[str, str], dataframe_name: str
    ) -> str:
        """
        Generates a corrected version of the failed code using the selected LLM.

        Args:
            question (str): The user's original question.
            code (str): The Python code that failed.
            error (str): The error message raised during execution.
            schema (Dict[str, str]): Column-name to description mapping for the DataFrame.
            dataframe_name (str): The variable name of the DataFrame in the code.

        Returns:
            str: The corrected Python code.
        """
        schema_description = "\n".join(f"- {col}: {desc}" for col, desc in schema.items())

        prompt = f"""
        You previously generated the following Python code to answer a user's question:

        Question:
        {question}

        Code (which failed to execute):
        ```python
        {code.strip()}
        ```

        The code failed with the following error:
        {error}

        Note that the DataFrame is named `{dataframe_name}` and its schema is:
        {schema_description}

        Fix the code based on the schema above. Do not reference non-existent columns.
        Return only the corrected Python code — no explanations or comments.
        """
        messages = [{"role": "user", "content": prompt}]
        return self.client.chat(messages)
