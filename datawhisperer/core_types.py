# Copyright 2024 JosueARz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import json

import pandas as pd


class InteractiveResponse:
    def __init__(
        self, text: str = "", value=None, code: str = "", table: pd.DataFrame = None, chart=None
    ):
        self.text = text or ""
        self.table = table
        self.chart = chart
        self.code = code
        self.value = self._build_value_json()

    def _build_value_json(self):
        return {
            "text": self.text,
            "table": self._serialize_table(),
            "chart": self._serialize_chart(),
        }

    def _serialize_table(self):
        if isinstance(self.table, pd.DataFrame):
            return self.table.to_dict(orient="records")
        return ""

    def _serialize_chart(self):
        if hasattr(self.chart, "to_plotly_json"):
            return self.chart.to_plotly_json()
        return ""

    def __str__(self):
        return self.text or "<No textual response>"

    def _repr_html_(self):
        from IPython.display import HTML

        html = ""

        # 1. Display text
        if self.text:
            html += f"<p><strong>📊 Response:</strong> {self.text}</p>"

        # 2. Display table
        if hasattr(self.table, "_repr_html_"):
            html += self.table._repr_html_()
        elif hasattr(self.table, "to_html"):
            html += self.table.to_html()

        # 3. Display chart if available
        if hasattr(self.chart, "_repr_html_"):
            html += self.chart._repr_html_()
        elif hasattr(self.chart, "show"):
            return self.chart.show()  # fallback in Jupyter

        return html
