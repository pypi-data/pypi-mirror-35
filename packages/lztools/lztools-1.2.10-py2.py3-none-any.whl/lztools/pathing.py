from pathlib import Path

def get_current_path():
    return str(Path(".").absolute())