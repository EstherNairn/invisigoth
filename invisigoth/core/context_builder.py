import os

def list_project_files(root="."):
    files = []
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            if f.endswith(".py") and not f.startswith("."):
                rel_path = os.path.relpath(os.path.join(dirpath, f), root)
                files.append(rel_path)
    return files

def build_context():
    files = list_project_files()
    file_summary = "\n".join(f"- {f}" for f in files)
    return f"Current Python files in project:\n{file_summary}"
