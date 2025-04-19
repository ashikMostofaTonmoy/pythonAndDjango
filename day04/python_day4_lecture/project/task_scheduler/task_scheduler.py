#!/usr/bin/env python3
"""
Task Scheduler

A command-line application that allows users to manage tasks with due dates.
Features:
- Add tasks with due dates
- Save tasks to a JSON file
- Load tasks from a JSON file
- List tasks sorted by due date
- Mark tasks as completed
- Filter tasks by status or date range

This project demonstrates the use of:
- Date and time handling
- JSON data processing
- Exception handling
- String formatting
- File I/O operations
"""

import json
import os
import datetime
import sys
from typing import List, Dict, Any, Optional


class Task:
    """Class representing a task with a title, description, due date, and status."""
    
    def __init__(self, title: str, description: str, due_date: datetime.datetime, 
                 completed: bool = False, task_id: Optional[int] = None):
        """
        Initialize a Task object.
        
        Args:
            title: The title of the task
            description: A detailed description of the task
            due_date: The due date and time for the task
            completed: Whether the task is completed (default: False)
            task_id: Unique identifier for the task (default: None, will be assigned by TaskManager)
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed
        self.task_id = task_id
        self.created_at = datetime.datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Task object to a dictionary for JSON serialization.
        
        Returns:
            A dictionary representation of the Task
        """
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat(),
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """
        Create a Task object from a dictionary.
        
        Args:
            data: Dictionary containing task data
            
        Returns:
            A Task object
        """
        return cls(
            title=data['title'],
            description=data['description'],
            due_date=datetime.datetime.fromisoformat(data['due_date']),
            completed=data['completed'],
            task_id=data['task_id']
        )
    
    def __str__(self) -> str:
        """
        Return a string representation of the Task.
        
        Returns:
            A formatted string with task details
        """
        status = "✓" if self.completed else "✗"
        due_date_str = self.due_date.strftime("%Y-%m-%d %H:%M")
        return f"[{status}] #{self.task_id}: {self.title} (Due: {due_date_str})"
    
    def details(self) -> str:
        """
        Return detailed information about the Task.
        
        Returns:
            A multi-line string with all task details
        """
        status = "Completed" if self.completed else "Pending"
        due_date_str = self.due_date.strftime("%Y-%m-%d %H:%M")
        created_at_str = self.created_at.strftime("%Y-%m-%d %H:%M")
        
        return (
            f"Task #{self.task_id}: {self.title}\n"
            f"Status: {status}\n"
            f"Due Date: {due_date_str}\n"
            f"Created: {created_at_str}\n"
            f"Description: {self.description}"
        )


class TaskManager:
    """Class for managing tasks, including saving/loading from JSON and filtering."""
    
    def __init__(self, filename: str = "tasks.json"):
        """
        Initialize a TaskManager object.
        
        Args:
            filename: The name of the JSON file to store tasks (default: "tasks.json")
        """
        self.tasks: List[Task] = []
        self.filename = filename
        self.next_id = 1
        
        # Try to load existing tasks
        try:
            self.load_tasks()
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is invalid, start with empty task list
            self.tasks = []
    
    def add_task(self, title: str, description: str, due_date: datetime.datetime) -> Task:
        """
        Add a new task to the task list.
        
        Args:
            title: The title of the task
            description: A detailed description of the task
            due_date: The due date and time for the task
            
        Returns:
            The newly created Task object
        """
        task = Task(title, description, due_date, task_id=self.next_id)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.
        
        Args:
            task_id: The ID of the task to find
            
        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def mark_task_completed(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id: The ID of the task to mark as completed
            
        Returns:
            True if the task was found and marked as completed, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            return True
        return False
    
    def mark_task_pending(self, task_id: int) -> bool:
        """
        Mark a task as pending (not completed).
        
        Args:
            task_id: The ID of the task to mark as pending
            
        Returns:
            True if the task was found and marked as pending, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was found and deleted, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            A list of all Task objects
        """
        return self.tasks
    
    def get_pending_tasks(self) -> List[Task]:
        """
        Get all pending (not completed) tasks.
        
        Returns:
            A list of pending Task objects
        """
        return [task for task in self.tasks if not task.completed]
    
    def get_completed_tasks(self) -> List[Task]:
        """
        Get all completed tasks.
        
        Returns:
            A list of completed Task objects
        """
        return [task for task in self.tasks if task.completed]
    
    def get_tasks_due_today(self) -> List[Task]:
        """
        Get all tasks due today.
        
        Returns:
            A list of Task objects due today
        """
        today = datetime.datetime.now().date()
        return [
            task for task in self.tasks 
            if task.due_date.date() == today
        ]
    
    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all overdue tasks (due date has passed and not completed).
        
        Returns:
            A list of overdue Task objects
        """
        now = datetime.datetime.now()
        return [
            task for task in self.tasks 
            if task.due_date < now and not task.completed
        ]
    
    def get_tasks_due_within_days(self, days: int) -> List[Task]:
        """
        Get all tasks due within a certain number of days.
        
        Args:
            days: Number of days from today
            
        Returns:
            A list of Task objects due within the specified days
        """
        now = datetime.datetime.now()
        end_date = now + datetime.timedelta(days=days)
        return [
            task for task in self.tasks 
            if now <= task.due_date <= end_date
        ]
    
    def get_tasks_by_date_range(self, start_date: datetime.datetime, 
                               end_date: datetime.datetime) -> List[Task]:
        """
        Get all tasks due within a date range.
        
        Args:
            start_date: The start date of the range
            end_date: The end date of the range
            
        Returns:
            A list of Task objects due within the specified date range
        """
        return [
            task for task in self.tasks 
            if start_date <= task.due_date <= end_date
        ]
    
    def sort_tasks_by_due_date(self, tasks: Optional[List[Task]] = None) -> List[Task]:
        """
        Sort tasks by due date (earliest first).
        
        Args:
            tasks: List of tasks to sort (default: all tasks)
            
        Returns:
            A sorted list of Task objects
        """
        if tasks is None:
            tasks = self.tasks
        return sorted(tasks, key=lambda task: task.due_date)
    
    def save_tasks(self) -> None:
        """
        Save all tasks to the JSON file.
        
        Raises:
            IOError: If there's an error writing to the file
        """
        try:
            with open(self.filename, 'w') as f:
                tasks_data = {
                    'next_id': self.next_id,
                    'tasks': [task.to_dict() for task in self.tasks]
                }
                json.dump(tasks_data, f, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}")
            raise
    
    def load_tasks(self) -> None:
        """
        Load tasks from the JSON file.
        
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
        """
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.next_id = data.get('next_id', 1)
                self.tasks = [Task.from_dict(task_data) for task_data in data.get('tasks', [])]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading tasks: {e}")
            raise


class TaskSchedulerCLI:
    """Command-line interface for the Task Scheduler application."""
    
    def __init__(self, task_manager: TaskManager):
        """
        Initialize the CLI with a TaskManager.
        
        Args:
            task_manager: The TaskManager to use
        """
        self.task_manager = task_manager
    
    def display_menu(self) -> None:
        """Display the main menu."""
        print("\n===== Task Scheduler =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Mark Task as Pending")
        print("5. Delete Task")
        print("6. Filter Tasks")
        print("7. View Task Details")
        print("8. Save Tasks")
        print("9. Exit")
        print("=========================")
    
    def get_date_input(self, prompt: str) -> datetime.datetime:
        """
        Get a date input from the user.
        
        Args:
            prompt: The prompt to display
            
        Returns:
            A datetime object
        """
        while True:
            try:
                date_str = input(prompt + " (YYYY-MM-DD HH:MM): ")
                return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
    
    def add_task(self) -> None:
        """Add a new task."""
        print("\n----- Add Task -----")
        title = input("Title: ")
        description = input("Description: ")
        due_date = self.get_date_input("Due Date")
        
        task = self.task_manager.add_task(title, description, due_date)
        print(f"\nTask added: {task}")
    
    def view_tasks(self, tasks: Optional[List[Task]] = None, title: str = "All Tasks") -> None:
        """
        Display a list of tasks.
        
        Args:
            tasks: The tasks to display (default: all tasks)
            title: The title to display above the task list
        """
        if tasks is None:
            tasks = self.task_manager.get_all_tasks()
        
        sorted_tasks = self.task_manager.sort_tasks_by_due_date(tasks)
        
        print(f"\n----- {title} -----")
        if not sorted_tasks:
            print("No tasks found.")
            return
        
        for task in sorted_tasks:
            print(task)
    
    def mark_task_completed(self) -> None:
        """Mark a task as completed."""
        print("\n----- Mark Task as Completed -----")
        self.view_tasks(self.task_manager.get_pending_tasks(), "Pending Tasks")
        
        try:
            task_id = int(input("\nEnter Task ID to mark as completed: "))
            if self.task_manager.mark_task_completed(task_id):
                print(f"Task #{task_id} marked as completed.")
            else:
                print(f"Task #{task_id} not found.")
        except ValueError:
            print("Invalid task ID. Please enter a number.")
    
    def mark_task_pending(self) -> None:
        """Mark a task as pending."""
        print("\n----- Mark Task as Pending -----")
        self.view_tasks(self.task_manager.get_completed_tasks(), "Completed Tasks")
        
        try:
            task_id = int(input("\nEnter Task ID to mark as pending: "))
            if self.task_manager.mark_task_pending(task_id):
                print(f"Task #{task_id} marked as pending.")
            else:
                print(f"Task #{task_id} not found.")
        except ValueError:
            print("Invalid task ID. Please enter a number.")
    
    def delete_task(self) -> None:
        """Delete a task."""
        print("\n----- Delete Task -----")
        self.view_tasks()
        
        try:
            task_id = int(input("\nEnter Task ID to delete: "))
            if self.task_manager.delete_task(task_id):
                print(f"Task #{task_id} deleted.")
            else:
                print(f"Task #{task_id} not found.")
        except ValueError:
            print("Invalid task ID. Please enter a number.")
    
    def filter_tasks(self) -> None:
        """Filter tasks by various criteria."""
        print("\n----- Filter Tasks -----")
        print("1. Show All Tasks")
        print("2. Show Pending Tasks")
        print("3. Show Completed Tasks")
        print("4. Show Tasks Due Today")
        print("5. Show Overdue Tasks")
        print("6. Show Tasks Due Within Days")
        print("7. Show Tasks in Date Range")
        print("8. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            self.view_tasks(title="All Tasks")
        elif choice == '2':
            self.view_tasks(self.task_manager.get_pending_tasks(), "Pending Tasks")
        elif choice == '3':
            self.view_tasks(self.task_manager.get_completed_tasks(), "Completed Tasks")
        elif choice == '4':
            self.view_tasks(self.task_manager.get_tasks_due_today(), "Tasks Due Today")
        elif choice == '5':
            self.view_tasks(self.task_manager.get_overdue_tasks(), "Overdue Tasks")
        elif choice == '6':
            try:
                days = int(input("Enter number of days: "))
                self.view_tasks(
                    self.task_manager.get_tasks_due_within_days(days),
                    f"Tasks Due Within {days} Days"
                )
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '7':
            try:
                start_date = self.get_date_input("Start Date")
                end_date = self.get_date_input("End Date")
                self.view_tasks(
                    self.task_manager.get_tasks_by_date_range(start_date, end_date),
                    f"Tasks Due Between {start_date.strftime('%Y-%m-%d')} and {end_date.strftime('%Y-%m-%d')}"
                )
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '8':
            return
        else:
            print("Invalid choice. Please try again.")
    
    def view_task_details(self) -> None:
        """View detailed information about a specific task."""
        print("\n----- View Task Details -----")
        self.view_tasks()
        
        try:
            task_id = int(input("\nEnter Task ID to view details: "))
            task = self.task_manager.get_task_by_id(task_id)
            if task:
                print("\n" + task.details())
            else:
                print(f"Task #{task_id} not found.")
        except ValueError:
            print("Invalid task ID. Please enter a number.")
    
    def save_tasks(self) -> None:
        """Save tasks to the JSON file."""
        try:
            self.task_manager.save_tasks()
            print("Tasks saved successfully.")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def run(self) -> None:
        """Run the CLI application."""
        print("Welcome to Task Scheduler!")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-9): ")
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.mark_task_completed()
            elif choice == '4':
                self.mark_task_pending()
            elif choice == '5':
                self.delete_task()
            elif choice == '6':
                self.filter_tasks()
            elif choice == '7':
                self.view_task_details()
            elif choice == '8':
                self.save_tasks()
            elif choice == '9':
                self.save_tasks()
                print("Thank you for using Task Scheduler. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    """Main function to run the Task Scheduler application."""
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set the JSON file path
    json_file = os.path.join(script_dir, "tasks.json")
    
    # Create a TaskManager with the JSON file
    task_manager = TaskManager(json_file)
    
    # Create and run the CLI
    cli = TaskSchedulerCLI(task_manager)
    cli.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)
