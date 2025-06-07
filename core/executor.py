from git_ops import commit_change
from llm import call_llm
import subprocess

def execute(goal):
    prompt = goal['prompt']
    filename = goal['filename']
    code = call_llm(prompt)
    with open(filename, "w") as f:
        f.write(code)
    passed = run_linter(filename)
    if passed:
        commit_change(filename, goal['description'])
        return "Committed"
    else:
        return "Linter failed"

def run_linter(path):
    result = subprocess.run(["flake8", path], capture_output=True)
    return result.returncode == 0
