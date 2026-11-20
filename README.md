# SWYNEX Python CLI Application – Task Manager

A beginner-friendly command-line task manager built with Python. It lets users add, view, complete, and delete tasks. Task data is stored locally in a JSON file, so it remains available after the application closes.

## Features

- Add a task with a title and optional description
- View all saved tasks and their status
- Mark a task as completed
- Delete a task
- Save and load data using JSON
- Validate task titles and task IDs
- Handle invalid input, missing tasks, file errors, and invalid JSON
- Organized into separate Python modules

## Project structure

```text
SWYNEX-Python-CLI-Application/
├── main.py             # Command-line menu and application entry point
├── task_manager.py     # Task operations and validation
├── storage.py          # JSON file handling
├── tasks.json          # Local task data
├── requirements.txt    # Dependencies (standard library only)
└── README.md           # Project documentation
```

## Requirements

- Python 3.9 or newer
- No external packages are required

Check your Python version:

```bash
python --version
```

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py` instead.

## Example menu

```text
========== SWYNEX TASK MANAGER ==========
1. Add task
2. View tasks
3. Mark task as completed
4. Delete task
5. Exit
=========================================
Choose an option (1-5):
```

## Example workflow

```text
Choose an option (1-5): 1
Enter task title: Learn Python functions
Enter task description (optional): Practice writing reusable functions
Task added successfully. Task ID: 1

Choose an option (1-5): 2

--------------- YOUR TASKS ---------------
ID: 1 | Learn Python functions | Pending
   Description: Practice writing reusable functions
------------------------------------------

Choose an option (1-5): 3
Enter the task ID to complete: 1
Task marked as completed.
```

## Concepts demonstrated

- **Functions:** reusable operations for each task action
- **Modules:** code separated into `main.py`, `task_manager.py`, and `storage.py`
- **Data structures:** lists and dictionaries
- **File handling:** reading and writing local files
- **JSON:** persistent structured storage
- **Validation:** checks for blank or overly long titles and invalid task IDs
- **Exception handling:** handles invalid input, missing tasks, malformed JSON, and file errors
- **Loops and conditionals:** interactive command-line menu

## Notes

- `tasks.json` is created automatically when the first task is saved if it does not already exist.
- Keep `tasks.json` in the project folder when running the program.
- If the JSON file becomes invalid, the program reports the issue instead of silently overwriting it.

## Internship task

Created as **Task 1 – Python CLI Application** for the SWYNEX Python Developer Internship.
