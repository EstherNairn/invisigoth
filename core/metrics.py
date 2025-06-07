"""
TokenTracker: Tracks LLM token usage across goals and enforces rate limits.
"""

import os
import json
from datetime import datetime
from pathlib import Path

USAGE_FILE = Path("metrics/token_usage.json")


class TokenTracker:
    def __init__(self, daily_limit, monthly_limit, per_goal_limit):
        self.daily_limit = daily_limit
        self.monthly_limit = monthly_limit
        self.per_goal_limit = per_goal_limit
        self.usage = {"daily": {}, "monthly": {}, "total": 0}
        self._load_usage()

    def _load_usage(self):
        if USAGE_FILE.exists():
            try:
                with open(USAGE_FILE, "r") as f:
                    self.usage = json.load(f)
            except Exception:
                pass

    def _save_usage(self):
        USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(USAGE_FILE, "w") as f:
            json.dump(self.usage, f, indent=2)

    def _get_today(self):
        return datetime.utcnow().strftime("%Y-%m-%d")

    def _get_month(self):
        return datetime.utcnow().strftime("%Y-%m")

    def update_usage(self, tokens_used: int):
        today = self._get_today()
        month = self._get_month()

        self.usage["daily"].setdefault(today, 0)
        self.usage["monthly"].setdefault(month, 0)

        self.usage["daily"][today] += tokens_used
        self.usage["monthly"][month] += tokens_used
        self.usage["total"] += tokens_used

        self._save_usage()

    def check_limits(self, tokens_needed: int) -> bool:
        today = self._get_today()
        month = self._get_month()

        used_today = self.usage["daily"].get(today, 0)
        used_month = self.usage["monthly"].get(month, 0)

        if used_today + tokens_needed > self.daily_limit:
            return False
        if used_month + tokens_needed > self.monthly_limit:
            return False
        if tokens_needed > self.per_goal_limit:
            return False
        return True
