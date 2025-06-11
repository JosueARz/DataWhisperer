# Changelog — datawhisperer

All notable changes to the `datawhisperer` library will be documented in this file.

---

## \[v0.1.4] - 2025-05-29

Initial public release of `datawhisperer`.

### Added

* Conversational natural language interface for working with `pandas` DataFrames.
* Support for LLMs like OpenAI and Gemini (Google Generative AI).
* Auto-generated Plotly visualizations (only when requested).
* Modular architecture with the following components:

  * `prompt_engine`: schema-aware prompt generation.
  * `code_executor`: safe code execution with auto-repair.
  * `llm_client`: clean interface to OpenAI and Gemini models.
* Developer tooling:

  * Testing: `pytest`, `pytest-cov`
  * Formatting: `black`, `isort`
* Packaging via `pyproject.toml` using `setuptools`.

### Improved

* Automatic DataFrame detection and prompt caching.
* Stable test coverage across critical modules (`executor`, `fixer`, `chatbot`).

### New

* `max_retries` parameter: automatic retry loop for failed code generations inside `run_with_repair()`.
* Retry logic integrated with `DataFrameChatbot` constructor (e.g., `max_retries=3`).
* Errors from code execution now trigger multiple repair attempts using the most recent feedback.

---

For usage details and architecture overview, see the [README](./README.md).
