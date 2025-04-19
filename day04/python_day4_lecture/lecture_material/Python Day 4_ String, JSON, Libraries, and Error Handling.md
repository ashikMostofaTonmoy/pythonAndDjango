# Python Day 4: String, JSON, Libraries, and Error Handling

## Table of Contents
1. [Strings and String Formatting](#strings-and-string-formatting)
2. [Iterators and Modules](#iterators-and-modules)
3. [Date and Time](#date-and-time)
4. [Math Module](#math-module)
5. [JSON in Python](#json-in-python)
6. [Regular Expressions (Regex)](#regular-expressions-regex)
7. [Exception Handling (Try and Except)](#exception-handling-try-and-except)
8. [Libraries and Modules](#libraries-and-modules)
9. [Real-life Projects](#real-life-projects)

---

## Strings and String Formatting

### String Basics

Strings in Python are sequences of characters enclosed in quotes (single, double, or triple quotes).

```python
# String creation
single_quoted = 'Hello, World!'
double_quoted = "Hello, World!"
triple_quoted = '''This is a multi-line
string that spans
multiple lines.'''

# String length
print(len(single_quoted))  # Output: 13

# Accessing characters (indexing)
print(single_quoted[0])    # Output: H
print(single_quoted[-1])   # Output: ! (negative indexing starts from the end)

# Slicing
print(single_quoted[0:5])  # Output: Hello
print(single_quoted[:5])   # Output: Hello (omitting start index defaults to 0)
print(single_quoted[7:])   # Output: World! (omitting end index goes to the end)
print(single_quoted[::2])  # Output: Hlo ol! (step by 2)
```

### String Methods

Python provides many built-in methods for string manipulation:

```python
text = "hello, world!"

# Case conversion
print(text.upper())        # Output: HELLO, WORLD!
print(text.lower())        # Output: hello, world!
print(text.capitalize())   # Output: Hello, world!
print(text.title())        # Output: Hello, World!

# Finding and counting
print(text.find("world"))  # Output: 7 (index where "world" starts)
print(text.count("l"))     # Output: 3 (number of occurrences of "l")

# Checking string properties
print("hello".isalpha())   # Output: True (contains only alphabetic characters)
print("123".isdigit())     # Output: True (contains only digits)
print("hello123".isalnum())# Output: True (contains alphanumeric characters)
print("   ".isspace())     # Output: True (contains only whitespace)

# Stripping whitespace
text_with_spaces = "   hello, world!   "
print(text_with_spaces.strip())    # Output: "hello, world!"
print(text_with_spaces.lstrip())   # Output: "hello, world!   " (left strip)
print(text_with_spaces.rstrip())   # Output: "   hello, world!" (right strip)

# Replacing text
print(text.replace("world", "Python"))  # Output: hello, Python!

# Splitting and joining
words = text.split(", ")   # Output: ['hello', 'world!']
print(", ".join(["hello", "Python"]))  # Output: hello, Python
```

### String Formatting

Python offers several ways to format strings:

#### 1. Using the `%` Operator (Old Style)

```python
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))
# Output: My name is Alice and I am 30 years old.
```

Common format specifiers:
- `%s` - String
- `%d` - Integer
- `%f` - Float
- `%.2f` - Float with 2 decimal places

#### 2. Using the `format()` Method

```python
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Bob and I am 25 years old.

# With positional arguments
print("My name is {0} and I am {1} years old.".format(name, age))
# Output: My name is Bob and I am 25 years old.

# With named arguments
print("My name is {name} and I am {age} years old.".format(name=name, age=age))
# Output: My name is Bob and I am 25 years old.

# Formatting numbers
print("Pi is approximately {:.2f}".format(3.14159))
# Output: Pi is approximately 3.14
```

#### 3. Using f-strings (Formatted String Literals, Python 3.6+)

```python
name = "Charlie"
age = 35
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Charlie and I am 35 years old.

# Expressions inside f-strings
print(f"In 5 years, I will be {age + 5} years old.")
# Output: In 5 years, I will be 40 years old.

# Formatting numbers
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")
# Output: Pi is approximately 3.14
```

### String Concatenation

```python
# Using the + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

# Using join() method
full_name = " ".join([first_name, last_name])
print(full_name)  # Output: John Doe

# Using f-strings
full_name = f"{first_name} {last_name}"
print(full_name)  # Output: John Doe
```

---

## Iterators and Modules

### Iterators

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values. In Python, an iterator is an object which implements the iterator protocol, which consists of the methods `__iter__()` and `__next__()`.

```python
# Using an iterator
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)  # Get an iterator

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4
print(next(my_iter))  # Output: 5
# print(next(my_iter))  # This would raise StopIteration
```

#### Creating a Custom Iterator

```python
class CountDown:
    def __init__(self, start):
        self.start = start
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Using our custom iterator
countdown = CountDown(5)
for num in countdown:
    print(num)  # Output: 5, 4, 3, 2, 1
```

### Generators

Generators are a simple way of creating iterators. A generator is a function that returns an object (iterator) which we can iterate over. It generates values on the fly and doesn't store them in memory.

```python
# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
for num in countdown(5):
    print(num)  # Output: 5, 4, 3, 2, 1

# Generator expression (similar to list comprehension)
squares = (x**2 for x in range(1, 6))
for square in squares:
    print(square)  # Output: 1, 4, 9, 16, 25
```

### Modules

A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py`.

#### Importing Modules

```python
# Import the entire module
import math
print(math.sqrt(16))  # Output: 4.0

# Import specific functions from a module
from math import sqrt, pi
print(sqrt(16))       # Output: 4.0
print(pi)             # Output: 3.141592653589793

# Import with an alias
import math as m
print(m.sqrt(16))     # Output: 4.0

# Import all functions from a module (not recommended)
from math import *
print(sqrt(16))       # Output: 4.0
```

#### Creating Your Own Module

You can create your own module by saving a Python file with functions and variables.

```python
# File: mymodule.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
```

```python
# Using your module
import mymodule

print(mymodule.greet("Alice"))  # Output: Hello, Alice!
print(mymodule.add(5, 3))       # Output: 8
print(mymodule.PI)              # Output: 3.14159
```

#### The `dir()` Function

The `dir()` function returns a list of all the attributes and methods available in an object:

```python
import math
print(dir(math))  # Lists all functions and variables in the math module
```

---

## Date and Time

Python's `datetime` module provides classes for manipulating dates and times.

### Basic Date and Time Operations

```python
import datetime

# Current date and time
now = datetime.datetime.now()
print(now)  # Output: 2023-04-19 13:30:45.123456

# Creating date objects
date1 = datetime.date(2023, 4, 19)
print(date1)  # Output: 2023-04-19

# Creating time objects
time1 = datetime.time(13, 30, 45)
print(time1)  # Output: 13:30:45

# Creating datetime objects
dt1 = datetime.datetime(2023, 4, 19, 13, 30, 45)
print(dt1)  # Output: 2023-04-19 13:30:45

# Current date
today = datetime.date.today()
print(today)  # Output: 2023-04-19

# Date components
print(today.year)    # Output: 2023
print(today.month)   # Output: 4
print(today.day)     # Output: 19

# Time components
print(now.hour)      # Output: 13
print(now.minute)    # Output: 30
print(now.second)    # Output: 45
```

### Date Formatting

```python
import datetime

now = datetime.datetime.now()

# Format date using strftime()
print(now.strftime("%Y-%m-%d"))  # Output: 2023-04-19
print(now.strftime("%d/%m/%Y"))  # Output: 19/04/2023
print(now.strftime("%B %d, %Y")) # Output: April 19, 2023
print(now.strftime("%H:%M:%S"))  # Output: 13:30:45
print(now.strftime("%I:%M %p"))  # Output: 01:30 PM

# Common format codes:
# %Y - Year with century (e.g., 2023)
# %m - Month as a number (01-12)
# %d - Day of the month (01-31)
# %B - Full month name (e.g., April)
# %b - Abbreviated month name (e.g., Apr)
# %A - Full weekday name (e.g., Wednesday)
# %a - Abbreviated weekday name (e.g., Wed)
# %H - Hour (00-23)
# %I - Hour (01-12)
# %M - Minute (00-59)
# %S - Second (00-59)
# %p - AM/PM
```

### Parsing Dates from Strings

```python
import datetime

# Parse date string using strptime()
date_string = "19 April, 2023"
date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print(date_object)  # Output: 2023-04-19 00:00:00

date_string = "04/19/2023 13:30:45"
date_object = datetime.datetime.strptime(date_string, "%m/%d/%Y %H:%M:%S")
print(date_object)  # Output: 2023-04-19 13:30:45
```

### Date Arithmetic

```python
import datetime

today = datetime.date.today()
print(today)  # Output: 2023-04-19

# Adding days
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)  # Output: 2023-04-20

# Subtracting days
yesterday = today - datetime.timedelta(days=1)
print(yesterday)  # Output: 2023-04-18

# Adding hours, minutes, seconds
now = datetime.datetime.now()
future = now + datetime.timedelta(hours=2, minutes=30)
print(future)  # Output: 2023-04-19 16:00:45 (assuming now is 13:30:45)

# Difference between dates
date1 = datetime.date(2023, 4, 19)
date2 = datetime.date(2023, 5, 1)
delta = date2 - date1
print(delta.days)  # Output: 12
```

### Working with Time Zones

```python
import datetime
import pytz  # You may need to install this: pip install pytz

# Current time in UTC
utc_now = datetime.datetime.now(pytz.UTC)
print(utc_now)  # Output: 2023-04-19 13:30:45.123456+00:00

# Convert to a specific timezone
ny_timezone = pytz.timezone('America/New_York')
ny_time = utc_now.astimezone(ny_timezone)
print(ny_time)  # Output: 2023-04-19 09:30:45.123456-04:00

# List all available timezones
for tz in pytz.all_timezones[:5]:  # Just showing first 5
    print(tz)
```

---

## Math Module

Python's `math` module provides access to mathematical functions.

### Basic Math Functions

```python
import math

# Constants
print(math.pi)       # Output: 3.141592653589793
print(math.e)        # Output: 2.718281828459045

# Rounding functions
print(math.ceil(4.2))   # Output: 5 (rounds up)
print(math.floor(4.8))  # Output: 4 (rounds down)
print(math.trunc(4.8))  # Output: 4 (truncates decimal part)
print(round(4.8))       # Output: 5 (built-in function, rounds to nearest)

# Power and logarithmic functions
print(math.pow(2, 3))   # Output: 8.0 (2^3)
print(math.sqrt(16))    # Output: 4.0 (square root)
print(math.log(100, 10))# Output: 2.0 (log base 10)
print(math.log2(8))     # Output: 3.0 (log base 2)
print(math.log10(100))  # Output: 2.0 (log base 10)

# Trigonometric functions (angles in radians)
print(math.sin(math.pi/2))  # Output: 1.0
print(math.cos(math.pi))    # Output: -1.0
print(math.tan(math.pi/4))  # Output: 1.0
print(math.degrees(math.pi))# Output: 180.0 (convert radians to degrees)
print(math.radians(180))    # Output: 3.141592653589793 (convert degrees to radians)
```

### Statistical Functions

```python
import statistics

data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

# Basic statistics
print(statistics.mean(data))     # Output: 5.0 (average)
print(statistics.median(data))   # Output: 5.0 (middle value)
print(statistics.mode(data))     # Output: 5 (most common value)
print(statistics.stdev(data))    # Output: ~2.58 (standard deviation)
print(statistics.variance(data)) # Output: ~6.67 (variance)
```

### Random Module

```python
import random

# Random float between 0 and 1
print(random.random())  # Output: 0.123456789...

# Random float within a range
print(random.uniform(1, 10))  # Output: 5.123456789...

# Random integer within a range (inclusive)
print(random.randint(1, 10))  # Output: 7

# Random choice from a sequence
print(random.choice(['apple', 'banana', 'cherry']))  # Output: 'banana'

# Random sample from a sequence (without replacement)
print(random.sample([1, 2, 3, 4, 5], 3))  # Output: [3, 1, 5]

# Shuffle a list in place
deck = ['ace', 'king', 'queen', 'jack']
random.shuffle(deck)
print(deck)  # Output: ['king', 'ace', 'jack', 'queen']
```

---

## JSON in Python

JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.

### Converting Python Objects to JSON

```python
import json

# Python dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "languages": ["Python", "JavaScript", "C++"],
    "is_employee": True,
    "height": 1.85
}

# Convert Python object to JSON string
json_string = json.dumps(person)
print(json_string)
# Output: {"name": "John Doe", "age": 30, "city": "New York", "languages": ["Python", "JavaScript", "C++"], "is_employee": true, "height": 1.85}

# Pretty print with indentation
json_formatted = json.dumps(person, indent=4)
print(json_formatted)
# Output:
# {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York",
#     "languages": [
#         "Python",
#         "JavaScript",
#         "C++"
#     ],
#     "is_employee": true,
#     "height": 1.85
# }

# Sort keys alphabetically
json_sorted = json.dumps(person, indent=4, sort_keys=True)
print(json_sorted)
```

### Converting JSON to Python Objects

```python
import json

# JSON string
json_string = '{"name": "Jane Smith", "age": 25, "city": "London", "is_student": true}'

# Convert JSON string to Python object
person = json.loads(json_string)
print(person)  # Output: {'name': 'Jane Smith', 'age': 25, 'city': 'London', 'is_student': True}

# Access dictionary values
print(person["name"])  # Output: Jane Smith
print(person["age"])   # Output: 25
```

### Reading and Writing JSON Files

```python
import json

# Writing JSON to a file
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# Reading JSON from a file
with open("person.json", "r") as file:
    loaded_person = json.load(file)
    print(loaded_person)  # Output: {'name': 'John Doe', 'age': 30, 'city': 'New York'}
```

### JSON Data Types

JSON supports the following data types, which map to Python types:

| JSON Type | Python Type |
|-----------|-------------|
| object    | dict        |
| array     | list        |
| string    | str         |
| number (int) | int      |
| number (real) | float   |
| true      | True        |
| false     | False       |
| null      | None        |

---

## Regular Expressions (Regex)

Regular expressions are powerful patterns used to match character combinations in strings.

### Basic Pattern Matching

```python
import re

text = "The quick brown fox jumps over the lazy dog."

# Search for a pattern
match = re.search(r"fox", text)
if match:
    print("Pattern found:", match.group())  # Output: Pattern found: fox
    print("Position:", match.start())       # Output: Position: 16

# Find all occurrences
matches = re.findall(r"the", text, re.IGNORECASE)
print(matches)  # Output: ['The', 'the']

# Replace pattern
new_text = re.sub(r"fox", "cat", text)
print(new_text)  # Output: The quick brown cat jumps over the lazy dog.
```

### Metacharacters and Special Sequences

```python
import re

# . (dot) - Matches any character except newline
print(re.findall(r"b.t", "bit bat but bet"))  # Output: ['bit', 'bat', 'but', 'bet']

# ^ (caret) - Matches start of string
print(re.findall(r"^The", "The quick brown fox"))  # Output: ['The']

# $ (dollar) - Matches end of string
print(re.findall(r"dog\.$", "The lazy dog."))  # Output: ['dog.']

# * (asterisk) - Matches 0 or more occurrences
print(re.findall(r"ab*c", "ac abc abbc"))  # Output: ['ac', 'abc', 'abbc']

# + (plus) - Matches 1 or more occurrences
print(re.findall(r"ab+c", "ac abc abbc"))  # Output: ['abc', 'abbc']

# ? (question mark) - Matches 0 or 1 occurrence
print(re.findall(r"colou?r", "color colour"))  # Output: ['color', 'colour']

# {} (braces) - Matches specified number of occurrences
print(re.findall(r"a{2}", "a aa aaa"))  # Output: ['aa', 'aa']
print(re.findall(r"a{2,3}", "a aa aaa aaaa"))  # Output: ['aa', 'aaa', 'aaa']

# [] (square brackets) - Matches any character in the brackets
print(re.findall(r"[aeiou]", "apple"))  # Output: ['a', 'e']

# [^] - Matches any character NOT in the brackets
print(re.findall(r"[^aeiou]", "apple"))  # Output: ['p', 'p', 'l']

# | (pipe) - Alternation (OR)
print(re.findall(r"cat|dog", "I have a cat and a dog"))  # Output: ['cat', 'dog']

# () (parentheses) - Groups patterns
match = re.search(r"(\d+)-(\d+)-(\d+)", "Date: 2023-04-19")
if match:
    print(match.group(0))  # Output: 2023-04-19 (entire match)
    print(match.group(1))  # Output: 2023 (first group)
    print(match.group(2))  # Output: 04 (second group)
    print(match.group(3))  # Output: 19 (third group)

# Special sequences
# \d - Matches any decimal digit (0-9)
print(re.findall(r"\d+", "I have 3 apples and 5 oranges"))  # Output: ['3', '5']

# \D - Matches any non-digit character
print(re.findall(r"\D+", "I have 3 apples and 5 oranges"))  # Output: ['I have ', ' apples and ', ' oranges']

# \w - Matches any alphanumeric character (a-z, A-Z, 0-9, _)
print(re.findall(r"\w+", "Hello, World! 123"))  # Output: ['Hello', 'World', '123']

# \W - Matches any non-alphanumeric character
print(re.findall(r"\W+", "Hello, World! 123"))  # Output: [', ', '! ']

# \s - Matches any whitespace character (space, tab, newline)
print(re.findall(r"\s+", "Hello World\tPython\nProgramming"))  # Output: [' ', '\t', '\n']

# \S - Matches any non-whitespace character
print(re.findall(r"\S+", "Hello World"))  # Output: ['Hello', 'World']

# \b - Matches word boundary
print(re.findall(r"\bcat\b", "The cat sat on the catalog"))  # Output: ['cat']
```

### Regex Flags

```python
import re

text = "The quick brown FOX jumps over the lazy dog."

# re.IGNORECASE or re.I - Case-insensitive matching
print(re.findall(r"fox", text, re.IGNORECASE))  # Output: ['FOX']

# re.MULTILINE or re.M - ^ and $ match start/end of each line
multiline_text = "First line\nSecond line\nThird line"
print(re.findall(r"^.+$", multiline_text, re.MULTILINE))  
# Output: ['First line', 'Second line', 'Third line']

# re.DOTALL or re.S - Dot matches any character including newline
print(re.findall(r"First.+Third", multiline_text, re.DOTALL))  
# Output: ['First line\nSecond line\nThird']
```

### Practical Regex Examples

```python
import re

# Validating email addresses
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(is_valid_email("user@example.com"))  # Output: True
print(is_valid_email("invalid-email"))     # Output: False

# Extracting phone numbers
text = "Contact us at (123) 456-7890 or 987-654-3210"
phone_numbers = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
print(phone_numbers)  # Output: ['(123) 456-7890', '987-654-3210']

# Parsing log files
log_line = '192.168.1.1 - - [19/Apr/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326'
pattern = r'(\d+\.\d+\.\d+\.\d+).+\[(.+?)\].+"([A-Z]+) (.+?) HTTP.+?" (\d+) (\d+)'
match = re.search(pattern, log_line)
if match:
    ip = match.group(1)
    date = match.group(2)
    method = match.group(3)
    path = match.group(4)
    status = match.group(5)
    size = match.group(6)
    print(f"IP: {ip}, Date: {date}, Method: {method}, Path: {path}, Status: {status}, Size: {size}")
    # Output: IP: 192.168.1.1, Date: 19/Apr/2023:13:55:36 +0000, Method: GET, Path: /index.html, Status: 200, Size: 2326
```

---

## Exception Handling (Try and Except)

Exception handling allows you to gracefully handle errors that might occur during program execution.

### Basic Exception Handling

```python
# Without exception handling
# x = 10 / 0  # This would raise a ZeroDivisionError and crash the program

# With exception handling
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")  # Output: Error: Division by zero!

# Handling multiple exceptions
try:
    # This could raise different exceptions
    num = int(input("Enter a number: "))  # Let's say user enters "abc"
    result = 10 / num
except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Division by zero!")

# Catching any exception
try:
    # Some risky operation
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except Exception as e:
    print(f"An error occurred: {e}")  # Output: An error occurred: [Errno 2] No such file or directory: 'nonexistent_file.txt'
```

### The `else` and `finally` Clauses

```python
try:
    num = int(input("Enter a number: "))  # Let's say user enters "5"
    result = 10 / num
except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Division by zero!")
else:
    # This block executes if no exceptions were raised
    print(f"Result: {result}")  # Output: Result: 2.0
finally:
    # This block always executes, regardless of whether an exception was raised
    print("Execution completed.")  # Output: Execution completed.
```

### Raising Exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is too high")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")  # Output: Validation error: Age cannot be negative
```

### Creating Custom Exceptions

```python
class CustomError(Exception):
    """Base class for custom exceptions"""
    pass

class ValueTooSmallError(CustomError):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(CustomError):
    """Raised when the input value is too large"""
    pass

def validate_number(number):
    if number < 10:
        raise ValueTooSmallError("Number is too small, should be at least 10")
    if number > 100:
        raise ValueTooLargeError("Number is too large, should be at most 100")
    return number

try:
    validate_number(5)
except ValueTooSmallError as e:
    print(f"Error: {e}")  # Output: Error: Number is too small, should be at least 10
except ValueTooLargeError as e:
    print(f"Error: {e}")
```

### Context Managers with `with` Statement

The `with` statement is used with objects that support the context management protocol. It ensures that resources are properly managed (acquired and released).

```python
# File handling with context manager
try:
    with open("example.txt", "w") as file:
        file.write("Hello, World!")
    
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)  # Output: Hello, World!
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## Libraries and Modules

Python has a rich ecosystem of libraries and modules that extend its functionality.

### Standard Library Modules

Python comes with a comprehensive standard library that provides modules for various tasks:

```python
# os - Operating system interface
import os
print(os.getcwd())  # Output: Current working directory
print(os.listdir())  # Output: List of files in current directory

# sys - System-specific parameters and functions
import sys
print(sys.version)  # Output: Python version
print(sys.path)     # Output: Module search path

# collections - Specialized container datatypes
from collections import Counter, defaultdict, namedtuple

# Count occurrences of elements
counter = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Dictionary with default values
fruit_count = defaultdict(int)  # Default value is 0
fruit_count['apple'] += 1
print(fruit_count['apple'])    # Output: 1
print(fruit_count['banana'])   # Output: 0 (default value)

# Named tuple (like a lightweight class)
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('John', 30, 'New York')
print(person.name)  # Output: John
print(person.age)   # Output: 30

# itertools - Functions for efficient looping
import itertools

# Infinite counter
counter = itertools.count(start=1, step=2)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 3
print(next(counter))  # Output: 5

# Cycle through elements
cycle = itertools.cycle(['red', 'green', 'blue'])
print(next(cycle))  # Output: red
print(next(cycle))  # Output: green
print(next(cycle))  # Output: blue
print(next(cycle))  # Output: red

# Combinations and permutations
print(list(itertools.combinations('ABC', 2)))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(itertools.permutations('ABC', 2)))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

### Third-Party Libraries

Python's ecosystem includes thousands of third-party libraries for various purposes. Here are a few popular ones:

```python
# requests - HTTP library for making requests
# pip install requests
import requests
response = requests.get('https://api.github.com')
print(response.status_code)  # Output: 200
print(response.json())       # Output: JSON response from GitHub API

# pandas - Data analysis and manipulation
# pip install pandas
import pandas as pd
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)
print(df)
print(df.describe())  # Statistical summary

# numpy - Numerical computing
# pip install numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())  # Output: 3.0
print(arr.std())   # Output: 1.4142135623730951

# matplotlib - Data visualization
# pip install matplotlib
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Plot')
plt.savefig('plot.png')
```

### Virtual Environments

Virtual environments allow you to create isolated Python environments for different projects:

```bash
# Creating a virtual environment
python -m venv myenv

# Activating the virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate

# Installing packages in the virtual environment
pip install requests pandas numpy

# Deactivating the virtual environment
deactivate
```

### Package Management with pip

`pip` is the package installer for Python:

```bash
# Installing a package
pip install package_name

# Installing a specific version
pip install package_name==1.2.3

# Upgrading a package
pip install --upgrade package_name

# Uninstalling a package
pip uninstall package_name

# Listing installed packages
pip list

# Saving requirements to a file
pip freeze > requirements.txt

# Installing from requirements file
pip install -r requirements.txt
```

---

## Real-life Projects

### Task Scheduler with Dates and JSON Data

A task scheduler application that allows users to:
- Add tasks with due dates
- Save tasks to a JSON file
- Load tasks from a JSON file
- List tasks sorted by due date
- Mark tasks as completed
- Filter tasks by status or date range

### Regex-Based Log File Analyzer

A log file analyzer that:
- Parses log files using regular expressions
- Extracts important information (timestamps, IP addresses, error codes, etc.)
- Generates statistics and reports
- Filters logs based on various criteria
- Detects patterns or anomalies in the logs

These projects will be implemented in separate Python files with detailed documentation.

---

## Summary

In this lecture, we covered:

1. **Strings and String Formatting**
   - String basics, methods, and operations
   - Different ways to format strings (%, format(), f-strings)

2. **Iterators and Modules**
   - Creating and using iterators
   - Generators as simplified iterators
   - Importing and creating modules

3. **Date and Time**
   - Working with dates, times, and timedeltas
   - Formatting and parsing dates
   - Date arithmetic and timezones

4. **Math Module**
   - Mathematical functions and constants
   - Statistical functions
   - Random number generation

5. **JSON in Python**
   - Converting between Python objects and JSON
   - Reading and writing JSON files
   - JSON data types

6. **Regular Expressions (Regex)**
   - Pattern matching and metacharacters
   - Extracting information using groups
   - Practical regex examples

7. **Exception Handling (Try and Except)**
   - Catching and handling exceptions
   - Using else and finally clauses
   - Raising exceptions and creating custom exceptions

8. **Libraries and Modules**
   - Standard library modules
   - Third-party libraries
   - Virtual environments and package management

These concepts are fundamental to Python programming and will be applied in the real-life projects: Task Scheduler and Log File Analyzer.
