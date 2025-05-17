# Copyright 2024 JosueARz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Main orchestrator: chatbot to interact with a DataFrame using natural language."""

from typing import Optional, Dict
import pandas as pd
import inspect
from dataWhisperer.llm_client.openai_client import OpenAIClient
from dataWhisperer.llm_client.gemini_client import GeminiClient
from dataWhisperer.prompt_engine.prompt_factory import PromptFactory
from dataWhisperer.code_executor.executor import run_with_repair
from dataWhisperer.prompt_engine.prompt_cache import hash_schema, load_cached_prompt, save_cached_prompt
from dataWhisperer.core_types import InteractiveResponse


class DataFrameChatbot:
    def __init__(
        self,
        api_key: str,
        model: str,
        dataframe: Optional[pd.DataFrame] = None,
        schema: Optional[Dict[str, str]] = None,
        dataframe_name: Optional[str] = None
    ) -> None:
        self.api_key = api_key
        self.model = model
        self.schema = schema or {}

        # 🔍 Infer the DataFrame name if not provided
        if dataframe_name is None and dataframe is not None:
            frame = inspect.currentframe()
            try:
                outer_frame = frame.f_back
                for var_name, var_val in outer_frame.f_locals.items():
                    if var_val is dataframe:
                        dataframe_name = var_name
                        break
            finally:
                del frame

        if dataframe_name is None:
            raise ValueError("Could not infer the name of the DataFrame. Please provide it manually.")

        self.dataframe_name = dataframe_name
        self.client = self._init_llm_client(api_key, model)

        # 🧠 Cache the system prompt
        schema_hash = hash_schema(self.schema)
        cached_prompt = load_cached_prompt(schema_hash)

        if cached_prompt is None:
            prompt_factory = PromptFactory(api_key, model, dataframe_name, self.schema)
            system_prompt = prompt_factory.build_system_prompt()
            save_cached_prompt(schema_hash, system_prompt)
        else:
            system_prompt = cached_prompt

        self.system_prompt = system_prompt
        self.context = {dataframe_name: dataframe} if dataframe is not None else {}

    def _init_llm_client(self, api_key: str, model: str):
        """
        Initializes the appropriate LLM client based on the selected model.
        """
        if model.startswith("gemini"):
            return GeminiClient(api_key, model_name=model)
        return OpenAIClient(api_key, model=model)

    def ask(self, question: str) -> str:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": question}
        ]
        return self.client.chat(messages)

    def ask_and_run(self, question: str, debug: bool = False) -> InteractiveResponse:
        code = self.ask(question)

        if debug:
            print("🧠 Generated code:\n", code)

        text, table, chart, final_code, success = run_with_repair(
            code=code,
            question=question,
            context=self.context,
            schema=self.schema,
            dataframe_name=self.dataframe_name,
            api_key=self.api_key,
            model=self.model
        )

        return InteractiveResponse(
            text=text,
            value=table if table is not None else chart,
            code=final_code,
            table=table,
            chart=chart
        )
