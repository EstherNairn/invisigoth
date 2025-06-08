import os
import json
import time
import yaml
from invisigoth.core.llm import LLMClient

MASTER_PROMPT_FILE = os.path.join("memory", "master_prompt.txt")
CONFIG_FILE = os.path.join("config.yaml")
RATE_LIMIT_SECONDS = 30  # Wait 30 seconds between calls

_last_call = 0

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load()

def read_master_prompt():
    with open(MASTER_PROMPT_FILE, "r") as f:
        return f.read()

def generate_goals(context: str):
    global _last_call
    now = time.time()
    if now - _last_call < RATE_LIMIT_SECONDS:
        print("Rate limit hit. Skipping LLM call.")
        return []

    config = load_config()
    client = LLMClient(provider=config["llm"]["provider"], config=config["llm"])
    master_prompt = read_master_prompt()
    prompt = f"{master_prompt}\n\nContext:\n{context}\n\nGenerate 1–3 new goals in JSON format."

    raw_response = client.query(prompt)
    _last_call = time.time()

    try:
        goals_json = json.loads(raw_response)
        return goals_json if isinstance(goals_json, list) else []
    except json.JSONDecodeError:
        print("Failed to parse LLM response.")
        return []
