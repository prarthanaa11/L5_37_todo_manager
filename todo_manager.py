"""A simple task manager with JSON storage and task-priority management."""

import json
import secrets
from datetime import datetime

tasks = {}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def add_task(title, priority="medium", labels=None):
    """Add a task and return its unique ID."""
    task_id = len(tasks) + 1
    task_labels = list(labels) if labels is not None else []
    task_labels.append(priority)

    tasks[task_id] = {
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.now().isoformat(),
        "labels": task_labels,
    }
    return task_id


def complete_task(task_id):
    """Mark a task as completed and return whether it exists."""
    if task_id in tasks:
        tasks[task_id]["done"] = True
        return True

    print("No task with id", task_id)
    return False


def pending_tasks():
    """Return pending task titles sorted by priority."""
    pending = [
        task for task in tasks.values()
        if not task["done"]
    ]
    pending.sort(
        key=lambda task: PRIORITY_ORDER[task["priority"]]
    )
    return [task["title"] for task in pending]


def find_task(keyword):
    """Return the ID of the first matching task, or None."""
    for task_id, task in tasks.items():
        if keyword.lower() in task["title"].lower():
            return task_id
    return None


def save_tasks(file_name="tasks_data.json"):
    """Save all tasks to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def load_tasks(file_name="tasks_data.json"):
    """Load tasks from a JSON file and restore integer IDs."""
    with open(file_name, "r", encoding="utf-8") as file:
        loaded_tasks = json.load(file)

    return {
        int(task_id): task
        for task_id, task in loaded_tasks.items()
    }


def export_json(file_name="tasks.json"):
    """Export all tasks to a readable JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def main():
    """Demonstrate task creation, completion, search, and storage."""
    add_task("Submit lab report", "high")
    add_task("Buy groceries")
    add_task("Call plumber", "low")
    add_task("Book train tickets", "high")

    complete_task(2)
    complete_task(99)

    print("Pending tasks:", pending_tasks())
    print("Task ID for 'plumber':", find_task("plumber"))
    print("Task ID for 'gym':", find_task("gym"))

    pending = pending_tasks()
    if pending:
        suggestion = secrets.choice(pending)
        print("Try this next:", suggestion)

    save_tasks()
    restored = load_tasks()
    print("Tasks restored from file:", len(restored))

    export_json()
    print("Exported tasks to tasks.json")


if __name__ == "__main__":
    main()
