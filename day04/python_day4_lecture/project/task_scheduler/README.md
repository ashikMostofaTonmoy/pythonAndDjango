# Task Scheduler

A command-line application that allows users to manage tasks with due dates, demonstrating the use of dates, JSON data, and exception handling in Python.

## Features

- Add tasks with titles, descriptions, and due dates
- Save tasks to a JSON file
- Load tasks from a JSON file
- List tasks sorted by due date
- Mark tasks as completed or pending
- Delete tasks
- Filter tasks by:
  - Status (pending/completed)
  - Due date (today, within days)
  - Date range
  - Overdue tasks
- View detailed information about specific tasks

## Concepts Demonstrated

This project demonstrates several key Python concepts covered in the Day 4 lecture:

1. **Date and Time Handling**
   - Creating and manipulating datetime objects
   - Date arithmetic with timedelta
   - Date formatting and parsing
   - Comparing dates

2. **JSON Data Processing**
   - Converting Python objects to JSON (serialization)
   - Converting JSON to Python objects (deserialization)
   - Reading and writing JSON files
   - Custom JSON serialization for datetime objects

3. **Exception Handling**
   - Using try/except blocks to handle errors
   - Handling specific exceptions (FileNotFoundError, JSONDecodeError, etc.)
   - Proper error messages and recovery

4. **String Formatting**
   - Using f-strings for string interpolation
   - Formatting dates with strftime
   - Creating formatted output for the CLI

5. **Object-Oriented Programming**
   - Class definitions with proper encapsulation
   - Class methods and properties
   - Type hints for better code readability

## Project Structure

The project consists of three main classes:

1. **Task**: Represents a single task with properties like title, description, due date, and status.
2. **TaskManager**: Manages a collection of tasks, including saving/loading from JSON and filtering tasks.
3. **TaskSchedulerCLI**: Provides a command-line interface for interacting with the TaskManager.

## How to Run

1. Make sure you have Python 3.6 or higher installed
2. Navigate to the project directory
3. Run the script:
   ```
   python task_scheduler.py
   ```

## Usage Examples

### Adding a Task

```
===== Task Scheduler =====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Mark Task as Pending
5. Delete Task
6. Filter Tasks
7. View Task Details
8. Save Tasks
9. Exit
=========================

Enter your choice (1-9): 1

----- Add Task -----
Title: Complete Python assignment
Description: Finish the Day 4 programming exercises
Due Date (YYYY-MM-DD HH:MM): 2023-04-25 23:59

Task added: [✗] #1: Complete Python assignment (Due: 2023-04-25 23:59)
```

### Viewing Tasks

```
Enter your choice (1-9): 2

----- All Tasks -----
[✗] #1: Complete Python assignment (Due: 2023-04-25 23:59)
[✓] #2: Review lecture notes (Due: 2023-04-20 18:00)
[✗] #3: Prepare for quiz (Due: 2023-04-22 10:00)
```

### Filtering Tasks

```
Enter your choice (1-9): 6

----- Filter Tasks -----
1. Show All Tasks
2. Show Pending Tasks
3. Show Completed Tasks
4. Show Tasks Due Today
5. Show Overdue Tasks
6. Show Tasks Due Within Days
7. Show Tasks in Date Range
8. Back to Main Menu

Enter your choice (1-8): 6
Enter number of days: 7

----- Tasks Due Within 7 Days -----
[✗] #1: Complete Python assignment (Due: 2023-04-25 23:59)
[✓] #2: Review lecture notes (Due: 2023-04-20 18:00)
[✗] #3: Prepare for quiz (Due: 2023-04-22 10:00)
```

## JSON File Format

Tasks are stored in a JSON file with the following structure:

```json
{
    "next_id": 4,
    "tasks": [
        {
            "task_id": 1,
            "title": "Complete Python assignment",
            "description": "Finish the Day 4 programming exercises",
            "due_date": "2023-04-25T23:59:00",
            "completed": false,
            "created_at": "2023-04-19T14:30:00"
        },
        {
            "task_id": 2,
            "title": "Review lecture notes",
            "description": "Go through the Day 4 lecture material",
            "due_date": "2023-04-20T18:00:00",
            "completed": true,
            "created_at": "2023-04-19T14:35:00"
        },
        {
            "task_id": 3,
            "title": "Prepare for quiz",
            "description": "Study for the upcoming Python quiz",
            "due_date": "2023-04-22T10:00:00",
            "completed": false,
            "created_at": "2023-04-19T14:40:00"
        }
    ]
}
```

## Learning Objectives

By studying and modifying this project, students will learn:

1. How to work with dates and times in Python
2. How to serialize and deserialize Python objects to/from JSON
3. How to handle exceptions properly
4. How to create a command-line interface for a Python application
5. How to organize code using object-oriented programming principles
6. How to implement filtering and sorting functionality
7. How to persist data between program runs using file I/O
