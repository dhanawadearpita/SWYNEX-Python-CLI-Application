"""Business logic for creating and managing tasks."""

from storage import load_tasks, save_tasks


class TaskManager:
    """Manage task records stored in a JSON file."""

    def __init__(self, storage_file: str = "tasks.json") -> None:
        self.storage_file = storage_file
        self.tasks = load_tasks(self.storage_file)

    @staticmethod
    def _validate_title(title: str) -> str:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")
        if len(title.strip()) > 100:
            raise ValueError("Task title must be 100 characters or fewer.")
        return title.strip()

    def _save(self) -> None:
        save_tasks(self.storage_file, self.tasks)

    def add_task(self, title: str, description: str = "") -> dict:
        title = self._validate_title(title)
        if not isinstance(description, str):
            raise ValueError("Description must be text.")

        next_id = max((task["id"] for task in self.tasks), default=0) + 1
        task = {
            "id": next_id,
            "title": title,
            "description": description.strip(),
            "completed": False,
        }
        self.tasks.append(task)
        self._save()
        return task

    def get_all_tasks(self) -> list:
        return list(self.tasks)

    def complete_task(self, task_id: str) -> None:
        task = self._find_task(task_id)
        task["completed"] = True
        self._save()

    def delete_task(self, task_id: str) -> None:
        task = self._find_task(task_id)
        self.tasks.remove(task)
        self._save()

    def _find_task(self, task_id: str) -> dict:
        try:
            normalized_id = int(task_id)
        except (TypeError, ValueError):
            raise ValueError("Task ID must be a valid number.") from None

        for task in self.tasks:
            if task["id"] == normalized_id:
                return task
        raise KeyError(f"No task exists with ID {normalized_id}.")
