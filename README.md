# Invisigoth

Invisigoth is a self-bootstrapping AI coding assistant that iteratively improves its own codebase. It operates in a plan–execute–commit loop, generating, validating, and committing new code based on high-level goals and a configurable master prompt.

---

## ✅ Features

- **Modular LLM backend** via OpenRouter or mock clients.
- **Goals** are tracked as JSON objects with status, prompt, and dependency metadata.
- **Goal Dependency Resolution**: Goals with unmet dependencies are skipped until prerequisites are completed.
- **Autonomous Planning**: Automatically generates new goals using project state and commit history.
- **Smart Execution**: Executes, lints, tests, and commits changes atomically.
- **Branch Isolation (optional)**: Each goal can be processed in its own branch and merged on success.
- **Goal History Tracking**: Logs completed goals with timestamps and commit hashes to `memory/history.json`.
- **Web Dashboard (WIP)**: Basic FastAPI UI for monitoring goals, commits, and triggers.

---

## 📁 Project Structure

```
main.py                         → Main plan–execute loop
config.yaml                    → Model/provider settings
core/
├── planner.py                 → Pending and completed goal management
├── context_builder.py         → Scans repo to guide LLM
├── generator.py               → Dynamic goal generation engine
├── executor.py                → Handles prompt execution, linting, and tests
├── history.py                 → Tracks completed goals and metadata
├── llm.py                     → Abstract LLM provider interface
└── providers/
    ├── openrouter.py          → Real OpenRouter API interface
    └── mock.py                → Stub/mock for development
memory/
├── pending_goals.json         → Active goals
├── completed_goals.json       → Completed goals
├── history.json               → Execution logs of goal completions
└── master_prompt.txt          → Root prompt used to guide generation
web/
└── dashboard.py               → FastAPI-based dashboard (WIP)
```

---

## 🚀 Usage

1. Configure your model in `config.yaml`.
2. Add initial goals to `memory/pending_goals.json`.
3. Run Invisigoth:

```bash
python main.py
```

4. (Optional) Launch the web dashboard:

```bash
uvicorn web.dashboard:app --reload
```

---

## 🧪 Testing

- Invisigoth can generate unit tests for any goal targeting a file ending with `_test.py`.
- Tests use `pytest` conventions and are validated before commit.

---

## 📦 Goal Format

Each goal is a JSON object like:

```json
{
  "id": "goal-001",
  "description": "Implement history tracking module",
  "filename": "core/history.py",
  "prompt": "Write a module to track completed goals...",
  "dependencies": [],
  "status": "pending"
}
```

---

## 🧠 Philosophy

- **Atomic Commits**: Each commit matches one goal.
- **Fallback-Safe**: Handles errors gracefully and continues operating.
- **Self-Improving**: Master prompt + diffs + codebase shape what’s generated.
---

## 🧰 Setup Instructions (Debian/Linux)

1. Clone the repo and run the setup script:

```bash
./setup_venv.sh
```

2. Activate the virtual environment:

```bash
source venv/bin/activate
```

3. Run Invisigoth:

```bash
python main.py
```

4. (Optional) Start the web dashboard:

```bash
python webui/dashboard.py
```

---

## 📦 Python Dependencies

Dependencies are listed in `requirements.txt` and include:

- `Flask` — Web dashboard
- `flake8` — Code linting
- `PyYAML` — YAML config parsing
- `pytest` — Test generation and running

Install all with:

```bash
pip install -r requirements.txt
```


---

## 🚀 GitHub Deployment & Server Installation

To make this project easy to install and run on a remote Debian-based server:

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/invisigoth.git
cd invisigoth
```

### 2. Install and Run Invisigoth

```bash
./install.sh
```

This script will:

- Install required system packages (`python3`, `pip`, `venv`, etc.)
- Create and activate a Python virtual environment
- Install dependencies from `requirements.txt`
- Set up logs and copy the `systemd` service
- Start the Invisigoth service in the background

### 3. Configuration

Before running, configure your secrets and API keys:

#### Create `config.yaml`

Copy the example file and fill in your OpenRouter API key:

```bash
cp config.yaml.example config.yaml
```

#### (Optional) Use a `.env` File

Copy the example and fill in any sensitive values:

```bash
cp .env.example .env
```

---

## 🛠️ Running Invisigoth Manually

If you prefer not to use `systemd`, you can also run it manually:

```bash
source venv/bin/activate
python main.py
```

---

## 🔄 Systemd Management

```bash
sudo systemctl status invisigoth
sudo systemctl restart invisigoth
sudo journalctl -u invisigoth -f
```

---

