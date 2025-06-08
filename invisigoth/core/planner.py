import json
import os
from typing import List, Optional, Dict

# Define paths for memory files
MEMORY_DIR = "memory"
PENDING_FILE = os.path.join(MEMORY_DIR, "pending_goals.json")
COMPLETED_FILE = os.path.join(MEMORY_DIR, "completed_goals.json")


class Goal:
    """
    Represents a coding goal that Invisigoth will attempt to accomplish.
    """
    def __init__(self, goal_id: str, description: str, filename: str, prompt: str,
                 dependencies: List[str], status: str = "pending"):
        self.id = goal_id
        self.description = description
        self.filename = filename
        self.prompt = prompt
        self.dependencies = dependencies
        self.status = status

    def to_dict(self) -> Dict:
        """
        Serialize the Goal to a dictionary for JSON output.
        """
        return {
            "id": self.id,
            "description": self.description,
            "filename": self.filename,
            "prompt": self.prompt,
            "dependencies": self.dependencies,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: Dict):
        """
        Create a Goal object from a dictionary loaded from JSON.
        """
        return Goal(
            goal_id=data["id"],
            description=data["description"],
            filename=data["filename"],
            prompt=data["prompt"],
            dependencies=data.get("dependencies", []),
            status=data.get("status", "pending")
        )


def load_pending_goals() -> List[Goal]:
    """
    Load the list of pending goals from disk.
    """
    if not os.path.exists(PENDING_FILE):
        return []
    with open(PENDING_FILE, "r") as f:
        return [Goal.from_dict(entry) for entry in json.load(f)]


def save_pending_goals(goals: List[Goal]) -> None:
    """
    Save the current list of pending goals to disk.
    """
    with open(PENDING_FILE, "w") as f:
        json.dump([g.to_dict() for g in goals], f, indent=2)


def append_completed_goal(goal: Goal) -> None:
    """
    Append a completed goal to the completed goals file.
    """
    if not os.path.exists(COMPLETED_FILE):
        completed = []
    else:
        with open(COMPLETED_FILE, "r") as f:
            completed = json.load(f)

    completed.append(goal.to_dict())
    with open(COMPLETED_FILE, "w") as f:
        json.dump(completed, f, indent=2)


def get_next_goal() -> Optional[Goal]:
    """
    Return the next available pending goal, or None if no goals remain.
    """
    goals = load_pending_goals()
    return goals[0] if goals else None


def mark_goal_complete(goal_id: str) -> None:
    """
    Mark a goal as completed and move it to the completed goals file.
    """
    pending = load_pending_goals()
    updated = []
    completed_goal = None

    for goal in pending:
        if goal.id == goal_id:
            goal.status = "complete"
            completed_goal = goal
        else:
            updated.append(goal)

    if completed_goal:
        append_completed_goal(completed_goal)
        save_pending_goals(updated)

def append_pending_goals(goals: List[Goal]) -> None:
    """
    Append new goals to the pending goal queue.
    """
    existing = load_pending_goals()
    combined = existing + goals
    save_pending_goals(combined)
