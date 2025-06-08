import subprocess
import logging
from typing import List, Optional


def run_git_command(cmd: List[str], cwd: Optional[str] = None) -> subprocess.CompletedProcess:
    """Runs a git command and returns the CompletedProcess object."""
    try:
        result = subprocess.run(
            ["git"] + cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return result
    except subprocess.CalledProcessError as e:
        logging.error(f"Git command failed: {' '.join(cmd)}\n{e.stderr}")
        raise


def stage_files(files: List[str]) -> None:
    """Stages the given files for commit."""
    for file in files:
        run_git_command(["add", file])
        logging.info(f"Staged file: {file}")


def has_changes() -> bool:
    """Returns True if there are staged changes."""
    result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return result.returncode != 0


def commit_changes(message: str) -> None:
    """Commits staged changes with the given commit message."""
    if has_changes():
        run_git_command(["commit", "-m", message])
        logging.info(f"Committed with message: {message}")
    else:
        logging.info("No changes to commit.")


def get_current_branch() -> str:
    """Returns the current Git branch name."""
    result = run_git_command(["rev-parse", "--abbrev-ref", "HEAD"])
    return result.stdout.strip()


def get_last_commit_hash() -> str:
    """Returns the hash of the last commit."""
    result = run_git_command(["rev-parse", "HEAD"])
    return result.stdout.strip()
