# 📐 Invisigoth Architecture Overview

## 🧠 Design Philosophy

- Modularity first
- Fail-safe self-improvement loop
- Git-based commit tracking with metadata

## 🔄 Core Loop

1. **Planner** defines a list of goals.
2. **Generator** prompts an LLM to produce new code.
3. **Executor** lints, tests, and commits working code.
4. **Goal state** is updated: pending → completed.
5. **Loop** restarts with new goals.

## 🗃 Key Files

- `main.py`: Main entrypoint for the loop
- `core/*.py`: Modular subsystems
- `memory/`: JSON-backed goal and prompt state
- `pyproject.toml`: Editable dev install with dependency tracking

## 🔐 Security/Resilience

- All Git commits made with a defined identity
- LLM secrets and model config stored in `.env` and `config.yaml`
- Autonomously skips failed goals

## 📈 Planned Enhancements

- Token budget tracking
- Rate limiting
- Web dashboard (Flask or FastAPI)
- Agent memory/history graph
