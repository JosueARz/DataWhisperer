# Copyright 2024 JosueARz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import hashlib
import json
from pathlib import Path
from typing import Dict, Optional

CACHE_DIR = Path(".prompt_cache")
CACHE_DIR.mkdir(exist_ok=True)


def hash_schema(schema: Dict[str, str]) -> str:
    """
    Generates a deterministic hash from the schema dictionary.

    Args:
        schema (Dict[str, str]): Column schema dictionary.

    Returns:
        str: MD5 hash representing the schema.
    """
    schema_str = json.dumps(schema, sort_keys=True)
    return hashlib.md5(schema_str.encode()).hexdigest()


def load_cached_prompt(hash_value: str) -> Optional[str]:
    """
    Loads the cached prompt if it exists.

    Args:
        hash_value (str): The hash representing the schema.

    Returns:
        Optional[str]: Cached system prompt content or None.
    """
    cache_file = CACHE_DIR / f"{hash_value}.txt"
    return cache_file.read_text() if cache_file.exists() else None


def save_cached_prompt(hash_value: str, prompt: str) -> None:
    """
    Saves the generated system prompt locally to disk.

    Args:
        hash_value (str): The hash representing the schema.
        prompt (str): The system prompt content to store.
    """
    cache_file = CACHE_DIR / f"{hash_value}.txt"
    cache_file.write_text(prompt)
