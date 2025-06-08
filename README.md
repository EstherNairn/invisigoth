# 🧠 Invisigoth – Self-Bootstrapping AI Coding Assistant

Invisigoth is a self-improving AI agent that uses a plan–execute–commit loop to enhance its own capabilities. It operates using modular goals, dynamic prompting, and Git for self-tracking.

## 🛠️ Setup

```bash
./venv-setup.sh
```

This script creates a virtual environment, installs dependencies, and sets the module up in editable mode.

## 🚀 Running

```bash
./run.sh
```

Or manually:

```bash
source venv/bin/activate
python -m invisigoth.main
```

## 📦 Project Structure

```
invisigoth/
├── core/
│   ├── planner.py
│   ├── executor.py
│   ├── context_builder.py
│   ├── generator.py
│   └── llm.py
├── main.py
tests/
memory/
├── pending_goals.json
├── completed_goals.json
└── master_prompt.txt
```

## 🔧 Dependencies

- `rich` – Terminal UI output
- `pyyaml` – Configuration file support
- `pytest` – Testing framework
