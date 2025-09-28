from config.config_loader import get_config
from llm_providers.openai_provider import OpenAIProvider
from llm_providers.gemini_provider import GeminiProvider
from llm_providers.huggingface_provider import HuggingFaceProvider
from llm_providers.ollama_provider import OllamaProvider

class Agent:
    def __init__(self):
        cfg = get_config()
        provider_name = cfg["default_provider"]

        if provider_name == "openai":
            self.provider = OpenAIProvider()
        elif provider_name == "gemini":
            self.provider = GeminiProvider()
        elif provider_name == "huggingface":
            self.provider = HuggingFaceProvider()
        elif provider_name == "ollama":
            self.provider = OllamaProvider()
        else:
            raise ValueError(f"Unknown provider: {provider_name}")

    def run(self, prompt: str) -> str:
        return self.provider.generate(prompt)
