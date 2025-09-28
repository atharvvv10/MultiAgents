from transformers import pipeline
from llm_providers.base import BaseProvider
from config.config_loader import get_config

class HuggingFaceProvider(BaseProvider):
    def __init__(self):
        cfg = get_config()["providers"]["huggingface"]
        self.model = cfg["model"]
        self.generator = pipeline("text-generation", model=self.model)

    def generate(self, prompt: str) -> str:
        result = self.generator(prompt, max_length=200, num_return_sequences=1)
        return result[0]["generated_text"]
