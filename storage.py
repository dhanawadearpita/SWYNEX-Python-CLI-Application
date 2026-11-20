"""JSON file storage helpers for the task manager."""

import json
from pathlib import Path


def load_tasks(file_name: str) -> list:
    """Load tasks from JSON; return an empty list if the file is missing."""
    path = Path(file_name)

    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"{path} contains invalid JSON. Fix or remove the file and try again."
        ) from error

    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON list of tasks.")

    return data


def save_tasks(file_name: str, tasks: list) -> None:
    """Save tasks to JSON using readable formatting."""
    path = Path(file_name)
    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
