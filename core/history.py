"""
Track completed goals and their metadata (commit hash, timestamp, etc.).
"""

import json
import os
from datetime import datetime

HISTORY_FILE = os.path.join("memory", "history.json")


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def record_goal_completion(goal_id, description, filename, commit_hash):
    history = load_history()
    history.append({
        "id": goal_id,
        "description": description,
        "filename": filename,
        "commit": commit_hash,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })
    save_history(history)
