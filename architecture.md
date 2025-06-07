# Invisigoth System Architecture

## Overview
Invisigoth is a self-bootstrapping AI coding assistant that operates in a plan–execute–commit loop. It autonomously improves its own codebase using a goal-driven system backed by LLM-based code generation and Git versioning.

---

## 🧠 Core Loop (`main.py`)

```
main.py
 ├── planner         → Loads/saves goals (with dependency handling)
 ├── generator       → Builds new goals using prompts + file context + commit history
 ├── executor        → Executes goals: generate → write → lint → commit
 ├── version_control → Git abstraction for staging, committing, branching
 └── context_builder → Extracts .py files and diffs to give context to LLM
```

---

## 📝 Goal Format

Stored in `memory/pending_goals.json` and `completed_goals.json`.

Each goal is a JSON object:
```json
{
  "id": "goal-001",
  "description": "Implement goal dependency resolution",
  "filename": "core/planner.py",
  "prompt": "Add support for dependency tracking in the planner...",
  "dependencies": ["goal-000"],
  "status": "pending"
}
```

---

## 🔧 Configuration

Configuration is defined in `config.yaml` (excluded from Git) or `.env`:

```yaml
llm_provider: openrouter
api_key: YOUR_API_KEY
model: gpt-4
```

Use `config.yaml.example` and `.env.example` as templates.

---

## 🗂️ Directory Layout

```
invisigoth/
├── main.py
├── config.yaml.example
├── install.sh
├── core/
│   ├── planner.py          # Manages goal state, dependencies
│   ├── generator.py        # LLM prompt building and goal generation
│   ├── executor.py         # Applies generated changes
│   ├── version_control.py  # Handles git commit, branching, history
│   ├── history.py          # Tracks completed goals in memory/history.json
│   ├── context_builder.py  # Builds context for LLM based on codebase
│   └── llm.py              # Selects LLM provider (mock or OpenRouter)
│       └── providers/
│           ├── openrouter.py
│           └── mock.py
├── webui/
│   └── dashboard.py        # Flask-based UI dashboard
├── memory/
│   ├── pending_goals.json
│   ├── completed_goals.json
│   ├── history.json
│   └── master_prompt.txt
```

---

## 🧪 Optional Features

- **Unit test generation** for `_test.py` goals
- **Flask dashboard**: basic goal/commit overview and manual trigger
- **Git branch isolation**: one branch per goal (optional)
- **Goal history tracking**: `memory/history.json`
- **Systemd deployment**: installable as a background Linux service

---

## 🔒 Security and Deployment

- Secrets stored in `.env` or `config.yaml` (excluded from Git)
- Recommended deployment via `systemd` with a dedicated `invisigoth` user
- Logs should go in a `logs/` folder or `journalctl`

---

## 🚀 Execution Flow

1. Load and validate `pending_goals.json`
2. Skip any goals with unmet dependencies
3. Select the next available goal
4. Use `context_builder` to build context
5. Generate code using LLM provider
6. If file ends in `_test.py`, generate unit test
7. Lint generated code (`flake8`)
8. Commit using `version_control.py`
9. Log to `history.json`
10. Regenerate new goals if idle

---

## 📚 Philosophy

- Modular, composable, testable
- No hardcoded secrets or logic
- Readable by humans and LLMs alike
- Reinforces its own structure with each completed task
