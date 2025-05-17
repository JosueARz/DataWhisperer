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

# 🧪 Test Suite para DataWhisperer

Este directorio contiene pruebas unitarias para los módulos principales del proyecto `datawhisperer`. La suite está diseñada para garantizar la robustez de cada componente y facilitar su evolución segura.

---

## 📂 Estructura de Pruebas

- **`test_chatbot.py`**  
  Verifica que `DataFrameChatbot`:
  - Se inicializa correctamente
  - Maneja correctamente el `schema`
  - Permite el uso de `FakeClient` para evitar llamadas reales a la API
  - Infiera correctamente el nombre del DataFrame

- **`test_executor.py`**  
  Cubre a fondo:
  - Sanitización del código LLM (`sanitize_code`)
  - Ejecución segura (`run_user_code`)
  - Reparación automática (`run_with_repair`)
  - Detección de outputs (últimos `DataFrame`, `Plotly`, y expresiones)

- **`test_fixer.py`**  
  Valida que `CodeFixer`:
  - Genere prompts de reparación adecuados
  - Elija correctamente el cliente (`OpenAIClient` o `GeminiClient`)
  - Devuelva el código corregido esperado a partir de un error simulado

- **`test_prompt_factory.py`**  
  Asegura que `PromptFactory`:
  - Construya correctamente el mensaje del rol `system`
  - Utilice correctamente la descripción del `schema`
  - Sea testable mediante `FakeClient`

---

## 🚀 Ejecución de pruebas

### ▶️ Ejecutar todas las pruebas
```bash
pytest
pytest --cov=datawhisperer --cov-report=term-missing
```

### 📌 Notas
- Las pruebas evitan hacer llamadas reales a OpenAI o Gemini usando clases FakeClient.

- Todos los módulos pueden ser testeados de forma aislada.

- La cobertura actual supera el 65%, con especial foco en el núcleo del sistema.

- Se recomienda ejecutar las pruebas como parte del pipeline CI/CD.

## 🔒 License
This project is licensed under the Apache License 2.0 — you are free to use, modify, and distribute it as long as you credit the author.

© 2024 JosueARz

## 💬 Want to contribute?
PRs welcome! Help us make DataWhisperer smarter, faster, and friendlier.

## 🧙 Bonus: Why "Whisperer"?
Because unlike chatbots, this one understands data.