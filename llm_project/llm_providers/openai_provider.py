import openai
from llm_providers.base import BaseProvider
from config.config_loader import get_config

class OpenAIProvider(BaseProvider):
    def __init__(self):
        cfg = get_config()["providers"]["openai"]
        openai.api_key = cfg["api_key"]
        self.model = cfg["model"]

    def generate(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
