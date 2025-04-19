# Python Day 4: Quick Guide

## 1. Strings and Formatting

### Basic String Operations
```python
# String creation and basic operations
text = "Hello, World!"
print(len(text))          # Length: 13
print(text[0])           # First character: 'H'
print(text[-1])          # Last character: '!'
print(text[0:5])         # Slicing: 'Hello'

# String methods
print(text.upper())      # 'HELLO, WORLD!'
print(text.lower())      # 'hello, world!'
print(text.split(","))   # ['Hello', ' World!']
print("  hello  ".strip()) # 'hello'
```

### String Formatting
```python
# f-strings (Python 3.6+)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# format() method
print("My name is {} and I am {} years old.".format(name, age))

# % operator (old style)
print("My name is %s and I am %d years old." % (name, age))
```

## 2. JSON Handling

### Working with JSON
```python
import json

# Python to JSON
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(data)
print(json_string)

# JSON to Python
json_data = '{"name": "John", "age": 30, "city": "New York"}'
python_data = json.loads(json_data)
print(python_data["name"])
```

## 3. Regular Expressions

### Basic Pattern Matching
```python
import re

text = "The quick brown fox jumps over the lazy dog"

# Search for pattern
match = re.search(r"fox", text)
if match:
    print("Found:", match.group())

# Find all matches
matches = re.findall(r"the", text, re.IGNORECASE)
print(matches)

# Replace pattern
new_text = re.sub(r"fox", "cat", text)
print(new_text)
```

## 4. Exception Handling

### Try-Except Blocks
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")
```

## 5. Generators

### Creating and Using Generators
```python
# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using generator
for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1

# Generator expression
squares = (x**2 for x in range(1, 6))
for square in squares:
    print(square)  # 1, 4, 9, 16, 25
```

## Practice Programs

### 1. String Manipulation Challenge
```python
def string_operations():
    text = "Python Programming is Fun!"
    
    # Task 1: Convert to lowercase
    print(text.lower())
    
    # Task 2: Count vowels
    vowels = "aeiou"
    count = sum(1 for char in text.lower() if char in vowels)
    print(f"Number of vowels: {count}")
    
    # Task 3: Reverse the string
    print(text[::-1])
    
    # Task 4: Replace spaces with hyphens
    print(text.replace(" ", "-"))

string_operations()
```

### 2. JSON Data Manager
```python
import json

def json_manager():
    # Sample data
    students = [
        {"name": "Alice", "age": 20, "grade": "A"},
        {"name": "Bob", "age": 21, "grade": "B"},
        {"name": "Charlie", "age": 19, "grade": "A+"}
    ]
    
    # Save to file
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
    
    # Load from file
    with open("students.json", "r") as file:
        loaded_students = json.load(file)
        for student in loaded_students:
            print(f"{student['name']}: {student['grade']}")

json_manager()
```

### 3. Log Analyzer (Simple Version)
```python
import re
from collections import Counter

def analyze_logs():
    # Sample log entries
    logs = [
        "192.168.1.1 - - [19/Apr/2023:10:15:30] GET /index.html 200",
        "10.0.0.1 - - [19/Apr/2023:10:15:35] GET /style.css 200",
        "192.168.1.2 - - [19/Apr/2023:10:16:10] GET /script.js 404"
    ]
    
    # Count IPs
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_counter = Counter()
    
    for log in logs:
        ip_match = re.search(ip_pattern, log)
        if ip_match:
            ip_counter[ip_match.group()] += 1
    
    print("IP Address Counts:")
    for ip, count in ip_counter.items():
        print(f"{ip}: {count}")

analyze_logs()
```

### 4. Task Manager (Simple Version)
```python
import json
from datetime import datetime

class SimpleTaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, due_date):
        task = {
            "title": title,
            "due_date": due_date,
            "completed": False
        }
        self.tasks.append(task)
    
    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['title']} (Due: {task['due_date']})")
    
    def save_tasks(self, filename):
        with open(filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

def test_task_manager():
    manager = SimpleTaskManager()
    
    # Add some tasks
    manager.add_task("Complete Python assignment", "2023-04-25")
    manager.add_task("Study for exam", "2023-04-26")
    
    # List tasks
    print("Current Tasks:")
    manager.list_tasks()
    
    # Save tasks
    manager.save_tasks("tasks.json")

test_task_manager()
```

## Exercises

1. **String Exercise**: Write a function that takes a string and returns:
   - The number of words
   - The longest word
   - The most common letter

2. **JSON Exercise**: Create a program that:
   - Reads a JSON file of products
   - Calculates the total price
   - Finds the most expensive product

3. **Regex Exercise**: Write a program that:
   - Validates email addresses
   - Extracts phone numbers from text
   - Formats dates in a specific pattern

4. **Generator Exercise**: Create a generator that:
   - Generates Fibonacci numbers
   - Generates prime numbers
   - Generates a sequence of squares

Try these exercises and check your understanding of the concepts! 