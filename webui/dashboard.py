"""
Flask-based dashboard for Invisigoth AI assistant.
"""

from flask import Flask, jsonify, request
import json
import subprocess
import os

app = Flask(__name__)

@app.route("/goals/pending", methods=["GET"])
def get_pending_goals():
    with open("memory/pending_goals.json") as f:
        goals = json.load(f)
    return jsonify(goals)

@app.route("/goals/completed", methods=["GET"])
def get_completed_goals():
    with open("memory/completed_goals.json") as f:
        goals = json.load(f)
    return jsonify(goals)

@app.route("/commits/recent", methods=["GET"])
def get_recent_commits():
    try:
        result = subprocess.run(
            ["git", "log", "--pretty=format:%h - %s", "-n", "5"],
            stdout=subprocess.PIPE,
            text=True
        )
        return jsonify({"commits": result.stdout.split("\n")})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/trigger", methods=["POST"])
def manual_trigger():
    # Placeholder for manual goal execution
    return jsonify({"status": "manual trigger not implemented yet"})

if __name__ == "__main__":
    app.run(debug=True)
