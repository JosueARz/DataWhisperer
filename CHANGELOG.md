# Changelog — datawhisperer

Todas las versiones y cambios relevantes de la librería `datawhisperer`.

---

## [v0.1.3] - 2025-05-29

Versión inicial pública de `datawhisperer`.

###  Añadido
- Interfaz conversacional en lenguaje natural para trabajar con `DataFrames`.
- Soporte para modelos LLM como OpenAI y Gemini.
- Visualizaciones automáticas con Plotly (solo si son solicitadas).
- Arquitectura modular compuesta por:
  - `prompt_engine`: generación de prompts adaptativos.
  - `code_executor`: ejecución segura y autocorrección de código.
  - `llm_client`: comunicación con modelos locales o en la nube.
- Configuración de desarrollo con:
  - `pytest`, `pytest-cov`
  - `black`, `isort`
- Distribución basada en `pyproject.toml` con `setuptools`.

---

Para más información, consulta la documentación o el [README](./README.md).
