"""Entry point for the SWYNEX Python CLI Task Manager."""

from task_manager import TaskManager


def display_menu() -> None:
    print("\n========== SWYNEX TASK MANAGER ==========")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")
    print("=========================================")


def get_menu_choice() -> str:
    return input("Choose an option (1-5): ").strip()


def main() -> None:
    manager = TaskManager()

    print("Welcome to the SWYNEX Python CLI Task Manager!")

    while True:
        display_menu()
        choice = get_menu_choice()

        try:
            if choice == "1":
                title = input("Enter task title: ").strip()
                description = input("Enter task description (optional): ").strip()
                task = manager.add_task(title, description)
                print(f"Task added successfully. Task ID: {task['id']}")

            elif choice == "2":
                tasks = manager.get_all_tasks()
                if not tasks:
                    print("No tasks found. Add your first task!")
                else:
                    print("\n--------------- YOUR TASKS ---------------")
                    for task in tasks:
                        status = "Completed" if task["completed"] else "Pending"
                        print(f"ID: {task['id']} | {task['title']} | {status}")
                        if task["description"]:
                            print(f"   Description: {task['description']}")
                    print("------------------------------------------")

            elif choice == "3":
                task_id = input("Enter the task ID to complete: ").strip()
                manager.complete_task(task_id)
                print("Task marked as completed.")

            elif choice == "4":
                task_id = input("Enter the task ID to delete: ").strip()
                manager.delete_task(task_id)
                print("Task deleted successfully.")

            elif choice == "5":
                print("Thank you for using the SWYNEX Task Manager. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

        except ValueError as error:
            print(f"Input error: {error}")
        except KeyError as error:
            print(f"Task error: {error}")
        except OSError as error:
            print(f"File error: Could not save task data. Details: {error}")
        except Exception as error:
            # Last-resort handling keeps unexpected errors from crashing the menu.
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
