import json
from datetime import datetime


class SimpleTaskScheduler:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"

    def add_task(self, title, due_date):
        """Add a new task with title and due date"""
        task = {
            "title": title,
            "due_date": due_date,
            "completed": False
        }
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def list_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found!")
            return

        print("\nYour Tasks:")
        print("-" * 30)
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['title']} (Due: {task['due_date']})")

    def mark_completed(self, task_number):
        """Mark a task as completed"""
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(
                f"Task '{self.tasks[task_number - 1]['title']}' marked as completed!")
        else:
            print("Invalid task number!")

    def save_tasks(self):
        """Save tasks to a JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)
        print("Tasks saved successfully!")

    def load_tasks(self):
        """Load tasks from a JSON file"""
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("No saved tasks found. Starting with empty task list.")


def main():
    scheduler = SimpleTaskScheduler()
    scheduler.load_tasks()

    while True:
        print("\nSimple Task Scheduler")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Save Tasks")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            scheduler.add_task(title, due_date)

        elif choice == "2":
            scheduler.list_tasks()

        elif choice == "3":
            scheduler.list_tasks()
            task_num = int(input("Enter task number to mark as completed: "))
            scheduler.mark_completed(task_num)

        elif choice == "4":
            scheduler.save_tasks()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
