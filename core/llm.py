from core.providers.openrouter import OpenRouterClient
from core.providers.mock import MockClient

class LLMClient:
    def __init__(self, provider: str = "openrouter", config: dict = None):
        """
        Create an LLM client based on the provider string.
        """
        self.provider = provider
        self.config = config or {}

        if provider == "openrouter":
            self.client = OpenRouterClient(self.config)
        elif provider == "mock":
            self.client = MockClient()
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")

    def query(self, prompt: str) -> str:
        """
        Send a prompt to the LLM and return the response.
        """
        return self.client.query(prompt)
