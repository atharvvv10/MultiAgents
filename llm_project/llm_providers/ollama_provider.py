import subprocess
from llm_providers.base import BaseProvider
from config.config_loader import get_config

class OllamaProvider(BaseProvider):
    def __init__(self):
        cfg = get_config()["providers"]["ollama"]
        self.model = cfg["model"]

    def generate(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                ["ollama", "run", self.model],
                input=prompt.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )
            return result.stdout.decode("utf-8").strip()
        except subprocess.CalledProcessError as e:
            return f"[Ollama Error] {e.stderr.decode('utf-8')}"
