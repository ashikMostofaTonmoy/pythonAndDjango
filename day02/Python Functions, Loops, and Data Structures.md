# Python Functions, Loops, and Data Structures

## Introduction

Welcome to Day 2 of our Python programming course! Today, we'll explore essential Python concepts that form the building blocks of programming: functions, loops, and data structures. These concepts are fundamental to writing efficient, organized, and reusable code.

In this lecture, we'll cover:
- Functions: definition, parameters, return types
- Loops: While and For loops
- Data Structures: Lists, Tuples, Sets, and Dictionaries

Let's dive in!

## Functions in Python

Functions are reusable blocks of code designed to perform a specific task. They help organize code, make it reusable, and break down complex problems into smaller, manageable parts.

### Defining Functions

In Python, we define functions using the `def` keyword, followed by the function name and parentheses `()`.

```python
def greet():
    print("Hello, World!")
```

To call (execute) this function:

```python
greet()  # Output: Hello, World!
```

### Function Parameters

Functions can accept inputs called parameters (or arguments):

```python
def greet_person(name):
    print(f"Hello, {name}!")

# Call the function with an argument
greet_person("Alice")  # Output: Hello, Alice!
greet_person("Bob")    # Output: Hello, Bob!
```

#### Multiple Parameters

Functions can have multiple parameters:

```python
def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person("Charlie", 25)  # Output: Charlie is 25 years old.
```

#### Default Parameter Values

You can assign default values to parameters, which are used when no argument is provided:

```python
def greet_with_message(name, message="Good morning"):
    print(f"{message}, {name}!")

greet_with_message("David")  # Output: Good morning, David!
greet_with_message("Eve", "Good evening")  # Output: Good evening, Eve!
```

#### Keyword Arguments

You can specify which parameter gets which value using keyword arguments:

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(animal="dog", name="Rex")  # Output: I have a dog named Rex.
describe_pet(name="Whiskers", animal="cat")  # Output: I have a cat named Whiskers.
```

### Return Values

Functions can return values using the `return` statement:

```python
def add_numbers(a, b):
    return a + b

sum_result = add_numbers(5, 3)
print(sum_result)  # Output: 8
```

A function can return multiple values as a tuple:

```python
def get_dimensions():
    return 500, 300

width, height = get_dimensions()
print(f"Width: {width}, Height: {height}")  # Output: Width: 500, Height: 300
```

### Variable Scope

Variables defined inside a function have local scope (only accessible within the function):

```python
def calculate():
    local_var = 10
    print(local_var)  # This works

calculate()
# print(local_var)  # This would cause an error because local_var is not defined outside the function
```

Variables defined outside functions have global scope:

```python
global_var = 20

def print_global():
    print(global_var)  # This works because global_var is accessible inside the function

print_global()  # Output: 20
```

To modify a global variable inside a function, use the `global` keyword:

```python
counter = 0

def increment():
    global counter
    counter += 1
    print(counter)

increment()  # Output: 1
increment()  # Output: 2
```

### Docstrings

Docstrings are used to document what a function does:

```python
def square(n):
    """
    Return the square of a number.
    
    Args:
        n: The number to square
        
    Returns:
        The square of the input number
    """
    return n ** 2
```

### Lambda Functions

Lambda functions are small, anonymous functions defined with the `lambda` keyword:

```python
# Regular function
def double(x):
    return x * 2

# Equivalent lambda function
double_lambda = lambda x: x * 2

print(double(5))        # Output: 10
print(double_lambda(5)) # Output: 10
```

Lambda functions are often used with functions like `map()`, `filter()`, and `sorted()`:

```python
# Using lambda with map() to double all numbers in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

# Using lambda with filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Using lambda with sorted() to sort by second element
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
```

## Loops in Python

Loops allow you to execute a block of code multiple times. Python has two main types of loops: `for` loops and `while` loops.

### While Loops

A `while` loop executes a block of code as long as a condition is true:

```python
count = 1
while count <= 5:
    print(count)
    count += 1
# Output:
# 1
# 2
# 3
# 4
# 5
```

#### Infinite Loops

Be careful not to create infinite loops (loops that never end):

```python
# This would run forever if not stopped
# while True:
#     print("This is an infinite loop!")
```

#### Break Statement

The `break` statement exits a loop prematurely:

```python
count = 1
while True:
    print(count)
    count += 1
    if count > 5:
        break
# Output is the same as the first while loop example
```

#### Continue Statement

The `continue` statement skips the current iteration and moves to the next one:

```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:  # If count is even
        continue        # Skip the rest of this iteration
    print(count)
# Output:
# 1
# 3
# 5
# 7
# 9
```

### For Loops

A `for` loop iterates over a sequence (like a list, tuple, string, etc.):

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
```

#### Looping Through a String

```python
for char in "Python":
    print(char)
# Output:
# P
# y
# t
# h
# o
# n
```

#### Using range()

The `range()` function generates a sequence of numbers:

```python
# range(stop)
for i in range(5):  # 0 to 4
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# range(start, stop)
for i in range(2, 5):  # 2 to 4
    print(i)
# Output:
# 2
# 3
# 4

# range(start, stop, step)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
# Output:
# 0
# 2
# 4
# 6
# 8
```

#### Nested Loops

You can have loops inside loops:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("-----")
# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# -----
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# -----
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# -----
```

#### Loop with else

Both `for` and `while` loops can have an `else` clause that executes when the loop completes normally (not through a `break`):

```python
for i in range(5):
    print(i)
else:
    print("Loop completed!")
# Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed!

# With break
for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print("This won't print because the loop was exited with break")
# Output:
# 0
# 1
# 2
```

## Data Structures in Python

Python has several built-in data structures that help organize and manipulate data efficiently.

### Lists

Lists are ordered, mutable (changeable) collections that can contain elements of different types.

#### Creating Lists

```python
# Empty list
empty_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
```

#### Accessing Elements

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing (starts at 0)
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry

# Negative indexing (counts from the end)
print(fruits[-1])  # Output: elderberry
print(fruits[-2])  # Output: date

# Slicing
print(fruits[1:3])    # Output: ['banana', 'cherry']
print(fruits[:3])     # Output: ['apple', 'banana', 'cherry']
print(fruits[2:])     # Output: ['cherry', 'date', 'elderberry']
print(fruits[::2])    # Output: ['apple', 'cherry', 'elderberry']
```

#### Modifying Lists

```python
fruits = ["apple", "banana", "cherry"]

# Change an element
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Add elements
fruits.append("date")  # Add to end
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

fruits.insert(1, "apricot")  # Insert at position
print(fruits)  # Output: ['apple', 'apricot', 'blueberry', 'cherry', 'date']

more_fruits = ["elderberry", "fig"]
fruits.extend(more_fruits)  # Add multiple elements
print(fruits)  # Output: ['apple', 'apricot', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']

# Remove elements
fruits.remove("blueberry")  # Remove by value
print(fruits)  # Output: ['apple', 'apricot', 'cherry', 'date', 'elderberry', 'fig']

popped = fruits.pop(1)  # Remove by index and return
print(popped)  # Output: apricot
print(fruits)  # Output: ['apple', 'cherry', 'date', 'elderberry', 'fig']

del fruits[0]  # Delete by index
print(fruits)  # Output: ['cherry', 'date', 'elderberry', 'fig']

fruits.clear()  # Remove all elements
print(fruits)  # Output: []
```

#### List Operations

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Length
print(len(numbers))  # Output: 9

# Count occurrences
print(numbers.count(5))  # Output: 2

# Find index
print(numbers.index(9))  # Output: 5

# Sort
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]

# Reverse
numbers.reverse()
print(numbers)  # Output: [9, 6, 5, 5, 4, 3, 2, 1, 1]

# Copy
numbers_copy = numbers.copy()
```

#### List Comprehensions

List comprehensions provide a concise way to create lists:

```python
# Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Create a list of even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]

# Create a matrix (list of lists)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### Tuples

Tuples are ordered, immutable (unchangeable) collections that can contain elements of different types.

#### Creating Tuples

```python
# Empty tuple
empty_tuple = ()

# Tuple with elements
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Single element tuple (note the comma)
single = (1,)
```

#### Accessing Elements

Tuples use the same indexing and slicing as lists:

```python
coordinates = (10, 20, 30, 40, 50)

print(coordinates[0])    # Output: 10
print(coordinates[-1])   # Output: 50
print(coordinates[1:3])  # Output: (20, 30)
```

#### Tuple Operations

```python
coordinates = (10, 20, 30, 40, 50)

# Length
print(len(coordinates))  # Output: 5

# Count occurrences
print(coordinates.count(30))  # Output: 1

# Find index
print(coordinates.index(40))  # Output: 3

# Concatenation
more_coordinates = coordinates + (60, 70)
print(more_coordinates)  # Output: (10, 20, 30, 40, 50, 60, 70)

# Repetition
repeated = coordinates * 2
print(repeated)  # Output: (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
```

#### Why Use Tuples?

1. Tuples are faster than lists
2. Tuples protect data that shouldn't change
3. Tuples can be used as dictionary keys (lists cannot)

```python
# Tuple unpacking
point = (3, 4)
x, y = point
print(f"X: {x}, Y: {y}")  # Output: X: 3, Y: 4

# Swapping variables
a, b = 5, 10
a, b = b, a  # Swap using tuple unpacking
print(f"a: {a}, b: {b}")  # Output: a: 10, b: 5
```

### Sets

Sets are unordered collections of unique elements.

#### Creating Sets

```python
# Empty set (can't use {} as that creates an empty dictionary)
empty_set = set()

# Set with elements
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}

# Create a set from a list (removes duplicates)
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
```

#### Set Operations

```python
fruits = {"apple", "banana", "cherry"}

# Add elements
fruits.add("date")
print(fruits)  # Output might be: {'cherry', 'apple', 'date', 'banana'}

# Remove elements
fruits.remove("banana")  # Raises error if not found
print(fruits)  # Output might be: {'cherry', 'apple', 'date'}

fruits.discard("elderberry")  # No error if not found
```

#### Set Mathematical Operations

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (all elements from both sets)
print(set1 | set2)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.union(set2))  # Same as above

# Intersection (elements in both sets)
print(set1 & set2)  # Output: {4, 5}
print(set1.intersection(set2))  # Same as above

# Difference (elements in set1 but not in set2)
print(set1 - set2)  # Output: {1, 2, 3}
print(set1.difference(set2))  # Same as above

# Symmetric difference (elements in either set, but not in both)
print(set1 ^ set2)  # Output: {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))  # Same as above
```

#### Set Comprehensions

```python
# Create a set of squares
squares = {x**2 for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}

# Create a set of even numbers
evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens)  # Output: {2, 4, 6, 8, 10}
```

### Dictionaries

Dictionaries are unordered collections of key-value pairs.

#### Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}

# Dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Alternative way to create a dictionary
person = dict(name="Alice", age=30, city="New York")
```

#### Accessing Values

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Access by key
print(person["name"])  # Output: Alice

# Using get() (safer, returns None or default if key not found)
print(person.get("age"))  # Output: 30
print(person.get("country"))  # Output: None
print(person.get("country", "Unknown"))  # Output: Unknown
```

#### Modifying Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Add or update key-value pairs
person["email"] = "alice@example.com"
person["age"] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

# Remove key-value pairs
removed_value = person.pop("city")
print(removed_value)  # Output: New York
print(person)  # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

# Remove and return the last inserted key-value pair
last_item = person.popitem()
print(last_item)  # Output might be: ('email', 'alice@example.com')
print(person)  # Output might be: {'name': 'Alice', 'age': 31}

# Clear all items
person.clear()
print(person)  # Output: {}
```

#### Dictionary Operations

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys
keys = person.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])

# Get all values
values = person.values()
print(values)  # Output: dict_values(['Alice', 30, 'New York'])

# Get all key-value pairs as tuples
items = person.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Check if key exists
print("name" in person)  # Output: True
print("email" in person)  # Output: False

# Update with another dictionary
person.update({"email": "alice@example.com", "phone": "123-456-7890"})
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@example.com', 'phone': '123-456-7890'}
```

#### Nested Dictionaries

```python
# Dictionary of dictionaries
users = {
    "alice": {
        "age": 30,
        "email": "alice@example.com",
        "active": True
    },
    "bob": {
        "age": 25,
        "email": "bob@example.com",
        "active": False
    }
}

print(users["alice"]["email"])  # Output: alice@example.com
```

#### Dictionary Comprehensions

```python
# Create a dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create a dictionary from two lists
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
name_age = {name: age for name, age in zip(names, ages)}
print(name_age)  # Output: {'Alice': 30, 'Bob': 25, 'Charlie': 35}
```

## Practical Examples

Let's combine what we've learned to solve some practical problems.

### Example 1: Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# Create a temperature conversion table
print("Celsius to Fahrenheit Conversion Table")
print("-------------------------------------")
print("Celsius | Fahrenheit")
print("--------|------------")
for celsius in range(0, 101, 10):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:7d} | {fahrenheit:10.1f}")
```

### Example 2: Word Counter

```python
def count_words(text):
    """Count the frequency of each word in a text."""
    # Remove punctuation and convert to lowercase
    for char in ".,!?;:\"'()[]{}":
        text = text.replace(char, "")
    text = text.lower()
    
    # Split into words and count
    words = text.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Sample text
sample = "Python is amazing! Python is versatile and Python is easy to learn."

# Count words
result = count_words(sample)

# Display results
print("Word Frequency:")
for word, count in sorted(result.items()):
    print(f"{word}: {count}")
```

### Example 3: Student Grade Tracker

```python
def calculate_average(grades):
    """Calculate the average of a list of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def get_letter_grade(score):
    """Convert a numerical score to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Student data
students = {
    "Alice": [85, 90, 92, 88],
    "Bob": [72, 65, 70, 75],
    "Charlie": [95, 98, 93, 97],
    "David": [60, 55, 68, 63]
}

# Calculate and display student averages
print("Student Grade Summary")
print("---------------------")
print("Name     | Average | Letter Grade")
print("---------|---------|-------------")

for name, grades in students.items():
    average = calculate_average(grades)
    letter = get_letter_grade(average)
    print(f"{name:9} | {average:7.1f} | {letter}")

# Find the student with the highest average
best_student = ""
highest_average = 0

for name, grades in students.items():
    average = calculate_average(grades)
    if average > highest_average:
        highest_average = average
        best_student = name

print(f"\nHighest performing student: {best_student} with an average of {highest_average:.1f}")
```

## Conclusion

In this lecture, we've covered the fundamentals of Python functions, loops, and data structures. These concepts are essential building blocks for writing efficient and organized Python code.

Key takeaways:
- Functions help organize code and make it reusable
- Loops allow you to repeat code execution efficiently
- Lists are versatile, ordered, and mutable collections
- Tuples are ordered, immutable collections
- Sets are unordered collections of unique elements
- Dictionaries store data as key-value pairs

In the next part of our class, we'll apply these concepts to build a real-life project: a Student Grading System.
