import google.generativeai as genai
from llm_providers.base import BaseProvider
from config.config_loader import get_config

class GeminiProvider(BaseProvider):
    def __init__(self):
        cfg = get_config()["providers"]["gemini"]
        genai.configure(api_key=cfg["api_key"])
        self.model = cfg["model"]

    def generate(self, prompt: str) -> str:
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(prompt)
        return response.text
