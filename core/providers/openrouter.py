import requests
import logging

class OpenRouterClient:
    def __init__(self, config):
        self.api_key = config.get("api_key")
        self.model = config.get("model", "gpt-4-turbo")
        if not self.api_key:
            raise ValueError("OpenRouter API key is missing in config.")

    def query(self, prompt: str) -> str:
        """
        Query OpenRouter using the configured model.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        if response.status_code != 200:
            logging.error(f"OpenRouter API error: {response.status_code} {response.text}")
            raise RuntimeError("OpenRouter request failed")

        return response.json()["choices"][0]["message"]["content"]
