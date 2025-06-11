# 🗺️ Roadmap de Desarrollo — `datawhisperer`

Este documento describe las fases planeadas para la evolución de la librería `datawhisperer`, priorizando mejoras en extensibilidad, robustez y experiencia de usuario. El orden está basado en impacto, alineación con el objetivo central y facilidad de integración incremental.

---

## ✅ Versión actual: `v0.1.4`

- Generación de código Python conversacional.
- Reparación automática de código fallido (`CodeFixer`).
- Ejecutor seguro (`code_executor`) y detección de DataFrames generados.
- Soporte para OpenAI (>=1.0.0) y Gemini.
- Esquema dinámico (`PromptFactory`).
- Test suite funcional (pytest).
- Publicación en TestPyPI con `pyproject.toml`.

---

## 🥇 PRIORIDAD ALTA (Core y extensibilidad inmediata)

### 1. 🔁 Autoreparación con reintentos en `fixer.py`
- [ ] Mejorar el sistema `CodeFixer` para que:
  - Opcional: estrategia de retry con retroalimentación (refinamiento incremental).

### 2. 🔌 Soporte para múltiples clientes LLM
- [ ] Añadir soporte para **Claude**, **LLaMA 3**, **Mistral**, etc.
- [ ] Abstraer la lógica en una interfaz `LLMClient` para facilitar integración.

### 3. 🧠 Soporte completo para modo `sql` y `python-sql`
- [ ] Instrucciones específicas para generación de SQL o SQL con Python.
- [ ] Soporte conversacional que combine análisis con consultas.

### 4. 🗃️ Integración con múltiples motores de datos
- [ ] Soporte para bases como SQLite, DuckDB, Postgres, Snowflake.
- [ ] Mapear resultados SQL a DataFrame y ejecutar lógica conversacional sobre ellos.

### 5. 🧪 Ampliación de test suite
- [ ] Tests de integración y edge cases para:
  - `CodeFixer` con retries.
  - Nuevos modos (`sql`, `sql-python`).
  - Clientes LLM alternativos.

---

## 🥈 PRIORIDAD MEDIA (Usabilidad y productividad)

### 6. 🧩 Plugin System
- [ ] Hooks para modificar prompts, respuestas, código o resultados.
- [ ] Plugins para visualización, profiling o inspección de resultados.

### 7. 💻 Interfaz CLI y/o Streamlit
- [ ] CLI tipo `dw ask --mode=sql "¿Cuánto stock hay por almacén?"`.
- [ ] App visual mínima con historial y ejecución de código generada.

### 8. 🧾 Logging estructurado y auditoría
- [ ] Guardar inputs, prompts, código generado y errores como JSON.

### 9. 🧰 Exportación de código
- [ ] Permitir exportar a `.py` o `.ipynb` desde CLI o interfaz visual.

---

## 🥉 PRIORIDAD BAJA (Optimización y comunidad)

### 10. 🔍 Embeddings y comprensión semántica
- [ ] Uso de embeddings locales (e.g. `jina`) para mayor comprensión del schema y las preguntas.

### 11. 📚 Documentación profesional (MkDocs)
- [ ] Guía de inicio, referencia API y ejemplos avanzados.

### 12. 🌍 Internacionalización (i18n)
- [ ] Preguntas y respuestas en múltiples idiomas.

### 13. 🔐 Seguridad y sandboxing
- [ ] Opcional: ejecución de código en contenedores o entornos controlados.

---

## 🔖 Versiones esperadas

| Versión | Objetivo clave                                      |
|---------|-----------------------------------------------------|
| v0.2.0  | Soporte `sql`, `python-sql`, + cliente DuckDB       |
| v0.3.0  | Clientes LLM alternativos + autoreparación con retries |
| v0.4.0  | Interfaz CLI y/o visual                             |
| v0.5.0  | Plugin System + conectores externos                 |
| v1.0.0  | Estable, con documentación, plugins, seguridad y tests completos |

---
