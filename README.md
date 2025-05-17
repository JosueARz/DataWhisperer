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
pip install datawhisperer
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

## 🔒 License
This project is licensed under the Apache License 2.0 — you are free to use, modify, and distribute it as long as you credit the author.

© 2024 JosueARz

## 💬 Want to contribute?
PRs welcome! Help us make DataWhisperer smarter, faster, and friendlier.

## 🧙 Bonus: Why "Whisperer"?
Because unlike chatbots, this one understands data.