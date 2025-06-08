#!/bin/bash
set -e
echo "[*] Bootstrapping venv..."

PYTHON_BIN="/opt/homebrew/bin/python3.11"
VENV_DIR="venv"

if [ ! -x "$PYTHON_BIN" ]; then
    echo "[!] Python 3.11 not found. Try: brew install python@3.11"
    exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
    "$PYTHON_BIN" -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install -e .[dev]

echo "[✓] venv ready. Use 'source venv/bin/activate' to activate."
