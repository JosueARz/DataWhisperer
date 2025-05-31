# 🧠 DataWhisperer

**Talk to your DataFrame. Literally.**

`DataWhisperer` is a Python library that allows you to interact with `pandas` DataFrames using **natural language**, powered by **OpenAI** or **Google Gemini**. Ask complex questions, generate visualizations, and get executable Python code — all with a single sentence.

> ✨ No more hunting through column names or writing endless `.groupby()` chains. Just whisper to your data.

---

## 🚀 Key Features

- 🔗 **Natural Language Interface** to your data
- 📊 **Auto-generated visualizations** using Plotly
- 🛠️ **Smart code repair** if the LLM-generated code fails
- 🧠 **Supports OpenAI & Gemini** (Google Generative AI)
- 🧼 Zero configuration, just plug & ask

---

## 🧱 Installation

```bash
pip install -i https://test.pypi.org/simple/ datawhisperer
```

Requires Python 3.8+

Or, if you're developing locally:
```bash
git clone https://github.com/JosueARz/DataWhisperer.git
cd DataWhisperer
pip install -e .
```

## ⚡ Quick Start
```python
from datawhisperer import DataFrameChatbot
import pandas as pd

# Your DataFrame
df = pd.read_csv("sales_data.csv")

# Define schema (column descriptions)
schema = {
    "region": "Sales region (e.g., North, South)",
    "sales": "Total amount sold",
    "date": "Date of the transaction"
}

# Create the chatbot
bot = DataFrameChatbot(
    api_key="your-openai-or-gemini-key",
    model="gpt-4",  # or "gemini-1.5-flash"
    dataframe=df,
    schema=schema
)

# Ask your data anything
response = bot.ask_and_run("Show a bar chart of total sales per region")
response
```
## 🧠 What kind of questions can I ask?
- "Show the average sales by month."

- "Which region had the highest total revenue?"

- "Plot a line chart of sales over time."

- "How many transactions happened after July?"

DataWhisperer turns that into runnable Python code with results.

# 🧪 Test Suite for DataWhisperer

This directory contains unit tests for the core modules of the `datawhisperer` project.  
The test suite is designed to ensure the robustness of each component and support safe and reliable evolution of the codebase.

---

## 📂 Test Structure
- test_chatbot.py
     Verifies that DataFrameChatbot:

   - Initializes correctly

   - Handles the provided schema as expected

   - Allows the use of a FakeClient to avoid real API calls

   - Correctly infers the name of the DataFrame

- test_executor.py
     Thoroughly tests:

   - LLM code sanitization (sanitize_code)

   - Secure code execution (run_user_code)

   - Automatic code repair (run_with_repair)

   - Output detection (last DataFrame, Plotly charts, expressions)

- test_fixer.py
   Validates that CodeFixer:

   - Generates appropriate repair prompts

   - Correctly selects the client (OpenAIClient or GeminiClient)

   - Returns the expected fixed code based on simulated errors

- test_prompt_factory.py
    Ensures that PromptFactory:

   - Correctly builds the system role message

   - Properly uses the schema description

   - Is testable using a FakeClient


---

## 🚀 Run all tests

### ▶️ Run tests with coverage report
```bash
pytest
pytest --cov=datawhisperer --cov-report=term-missing
```

### 📌  Notes
- Tests avoid real calls to OpenAI or Gemini by using FakeClient classes.

- All modules are designed to be tested in isolation.

- Current test coverage exceeds 65%, with special focus on the system core.

- It is recommended to run tests as part of the CI/CD pipeline.


## 📋 Version History

See the [registro de cambios](./CHANGELOG.md) for a full list of updates and improvements.


## 🔒 License
This project is licensed under the Apache License 2.0 — you are free to use, modify, and distribute it as long as you credit the author.

© 2024 JosueARz

## 💬 Want to contribute?
PRs welcome! Help us make DataWhisperer smarter, faster, and friendlier.

## 🧙 Bonus: Why "Whisperer"?
Because unlike chatbots, this one understands data.
