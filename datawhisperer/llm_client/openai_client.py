# Copyright 2024 JosueARz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Minimal client for interacting with the OpenAI API."""

from typing import Dict, List
from openai import OpenAI

class OpenAIClient:
    """
    Cliente para enviar solicitudes de chat a la API de OpenAI utilizando el nuevo cliente OpenAI.
    """

    def __init__(self, api_key: str, model: str = "gpt-4.1-mini") -> None:
        """
        Inicializa el cliente con la clave de API proporcionada y el modelo especificado.

        Args:
            api_key (str): Clave de API de OpenAI.
            model (str): Modelo a utilizar (por defecto es "gpt-4.1-mini").
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def chat(self, messages: List[Dict[str, str]], temperature: float = 0.3) -> str:
        """
        Envía una lista de mensajes formateados para chat y devuelve la respuesta del modelo.

        Args:
            messages (List[Dict[str, str]]): Lista de mensajes como
                [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]
            temperature (float): Nivel de aleatoriedad de la respuesta.

        Returns:
            str: Contenido de texto de la respuesta del modelo.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
