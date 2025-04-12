# Object-Oriented Programming in Python

## Introduction to OOP

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code. It's designed to make complex code more manageable, reusable, and organized. Python is a versatile language that supports multiple programming paradigms, including OOP.

In this lecture, we'll cover:
- Lambda Functions
- Arrays (Lists in Python)
- Classes and Objects
- Inheritance
- Polymorphism

Let's dive in!

## Lambda Functions

Lambda functions are small, anonymous functions defined with the `lambda` keyword. They can take any number of arguments but can only have one expression.

### Syntax:
```python
lambda arguments: expression
```

### Examples:

1. **Simple lambda function:**
```python
# Regular function
def add(x, y):
    return x + y
    
# Equivalent lambda function
add_lambda = lambda x, y: x + y

# Using both functions
print(add(5, 3))        # Output: 8
print(add_lambda(5, 3)) # Output: 8
```

2. **Lambda with a single argument:**
```python
# Square a number
square = lambda x: x ** 2
print(square(4))  # Output: 16
```

3. **Lambda with no arguments:**
```python
# Return a greeting
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!
```

### Practical Uses of Lambda Functions:

1. **With `sorted()`:**
```python
# Sort a list of tuples by the second element
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

2. **With `filter()`:**
```python
# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

3. **With `map()`:**
```python
# Double each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]
```

## Arrays (Lists in Python)

In Python, we typically use lists as arrays. Lists are ordered, mutable collections that can contain elements of different types.

### Creating Lists:

```python
# Empty list
empty_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
```

### Accessing Elements:

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

### Common List Operations:

1. **Adding Elements:**
```python
fruits = ["apple", "banana", "cherry"]

# Append (add to end)
fruits.append("date")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Insert at specific position
fruits.insert(1, "apricot")
print(fruits)  # Output: ['apple', 'apricot', 'banana', 'cherry', 'date']

# Extend (add multiple elements)
more_fruits = ["elderberry", "fig"]
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'apricot', 'banana', 'cherry', 'date', 'elderberry', 'fig']
```

2. **Removing Elements:**
```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Remove by value
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'date', 'elderberry']

# Remove by index
removed_fruit = fruits.pop(1)
print(removed_fruit)  # Output: cherry
print(fruits)         # Output: ['apple', 'date', 'elderberry']

# Clear all elements
fruits.clear()
print(fruits)  # Output: []
```

3. **Other Operations:**
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

### List Comprehensions:

List comprehensions provide a concise way to create lists.

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

## Classes and Objects

Classes are blueprints for creating objects. They define attributes (data) and methods (functions) that the objects will have.

### Defining a Class:

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Initializer / Constructor
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
```

### Creating Objects (Instances):

```python
# Create Dog objects
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

# Access attributes
print(buddy.name)  # Output: Buddy
print(miles.age)   # Output: 4

# Access class attribute
print(buddy.species)  # Output: Canis familiaris
print(miles.species)  # Output: Canis familiaris

# Call methods
print(buddy.description())  # Output: Buddy is 9 years old
print(miles.speak("Woof"))  # Output: Miles says Woof
```

### Special (Magic/Dunder) Methods:

Python has special methods that start and end with double underscores. They allow you to define how objects of your class behave with built-in functions and operators.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    # Representation (for developers)
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    # Addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    # Equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Create Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Use special methods
print(p1)          # Output: Point(1, 2)
print(p1 + p2)     # Output: Point(4, 6)
print(p1 == Point(1, 2))  # Output: True
```

### Class Methods and Static Methods:

```python
class Person:
    count = 0  # Class attribute
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    
    # Instance method (has access to instance through self)
    def display(self):
        return f"{self.name} is {self.age} years old"
    
    # Class method (has access to class through cls)
    @classmethod
    def get_count(cls):
        return f"There are {cls.count} Person objects"
    
    # Static method (no access to instance or class)
    @staticmethod
    def is_adult(age):
        return age >= 18

# Create Person objects
p1 = Person("Alice", 25)
p2 = Person("Bob", 17)

# Call instance method
print(p1.display())  # Output: Alice is 25 years old

# Call class method
print(Person.get_count())  # Output: There are 2 Person objects

# Call static method
print(Person.is_adult(20))  # Output: True
print(p2.is_adult(p2.age))  # Output: False
```

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class. The original class is called the parent or base class, and the new class is called the child or derived class.

### Basic Inheritance:

```python
# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent class's __init__ method
        super().__init__(name, "Canis familiaris")
        self.breed = breed
    
    # Override parent method
    def make_sound(self):
        return "Woof!"
    
    # Add new method
    def wag_tail(self):
        return f"{self.name} wags tail"

# Create objects
generic_animal = Animal("Generic", "Animal species")
buddy = Dog("Buddy", "Golden Retriever")

# Use parent methods
print(generic_animal.info())  # Output: Generic is a Animal species
print(buddy.info())           # Output: Buddy is a Canis familiaris

# Use overridden method
print(generic_animal.make_sound())  # Output: Some generic animal sound
print(buddy.make_sound())           # Output: Woof!

# Use child-specific method
print(buddy.wag_tail())  # Output: Buddy wags tail
```

### Multiple Inheritance:

Python allows a class to inherit from multiple parent classes.

```python
class Swimmer:
    def swim(self):
        return "Swimming"

class Flyer:
    def fly(self):
        return "Flying"

# Multiple inheritance
class Duck(Swimmer, Flyer):
    def __init__(self, name):
        self.name = name
    
    def info(self):
        return f"{self.name} can swim and fly"

# Create Duck object
donald = Duck("Donald")

# Use methods from both parent classes
print(donald.swim())  # Output: Swimming
print(donald.fly())   # Output: Flying
print(donald.info())  # Output: Donald can swim and fly
```

### Method Resolution Order (MRO):

When a class inherits from multiple classes, Python uses the Method Resolution Order to determine which method to call.

```python
class A:
    def who_am_i(self):
        return "I am A"

class B(A):
    def who_am_i(self):
        return "I am B"

class C(A):
    def who_am_i(self):
        return "I am C"

class D(B, C):
    pass

# Create D object
d = D()

# Check MRO
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Call method
print(d.who_am_i())  # Output: I am B (from class B, not C)
```

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables using a single interface with different underlying forms.

### Polymorphism with Methods:

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Function that works with any Animal
def animal_sound(animal):
    return animal.speak()

# Create objects
dog = Dog()
cat = Cat()
duck = Duck()

# Polymorphic behavior
print(animal_sound(dog))   # Output: Woof!
print(animal_sound(cat))   # Output: Meow!
print(animal_sound(duck))  # Output: Quack!

# List of different animals
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(animal.speak())  # Each animal makes its own sound
```

### Duck Typing:

Python uses "duck typing" - if it walks like a duck and quacks like a duck, it's a duck. This means objects don't need to be from the same inheritance hierarchy to be used polymorphically.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Person:
    def speak(self):
        return "Hello!"

# Function that works with anything that has a speak method
def make_speak(entity):
    return entity.speak()

# Create objects
dog = Dog()
cat = Cat()
person = Person()

# Polymorphic behavior without inheritance
print(make_speak(dog))     # Output: Woof!
print(make_speak(cat))     # Output: Meow!
print(make_speak(person))  # Output: Hello!
```

## Practical Examples

### Example 1: Bank Account System

```python
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Amount must be positive"
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.balance}"
            return "Insufficient funds"
        return "Amount must be positive"
    
    def get_balance(self):
        return f"Current balance: ${self.balance}"
    
    def __str__(self):
        return f"Account {self.account_number} owned by {self.owner} with balance ${self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.01):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Added interest: ${interest:.2f}. New balance: ${self.balance}"

class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=100):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.balance}"
            return "Exceeds overdraft limit"
        return "Amount must be positive"

# Create accounts
savings = SavingsAccount("S123", "Alice", 1000, 0.05)
checking = CheckingAccount("C456", "Bob", 500, 200)

# Use accounts
print(savings)  # Output: Account S123 owned by Alice with balance $1000
print(savings.deposit(500))  # Output: Deposited $500. New balance: $1500
print(savings.add_interest())  # Output: Added interest: $75.00. New balance: $1575

print(checking)  # Output: Account C456 owned by Bob with balance $500
print(checking.withdraw(600))  # Output: Withdrew $600. New balance: $-100
print(checking.withdraw(300))  # Output: Exceeds overdraft limit
```

### Example 2: Shape Hierarchy

```python
import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def __str__(self):
        return f"Rectangle with length {self.length} and width {self.width}"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
    
    def __str__(self):
        return f"Square with side {self.side}"

# Create shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(4)

# Calculate areas and perimeters
shapes = [circle, rectangle, square]
for shape in shapes:
    print(f"{shape}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print()

# Output:
# Circle with radius 5
# Area: 78.54
# Perimeter: 31.42
#
# Rectangle with length 4 and width 6
# Area: 24.00
# Perimeter: 20.00
#
# Square with side 4
# Area: 16.00
# Perimeter: 16.00
```

### Example 3: Employee Management System

```python
class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
    
    def get_salary(self):
        return self.salary
    
    def __str__(self):
        return f"Employee {self.employee_id}: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, employee_id, name, salary, department):
        super().__init__(employee_id, name, salary)
        self.department = department
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
        return f"Added {employee.name} to {self.department} department"
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            return f"Removed {employee.name} from {self.department} department"
        return f"{employee.name} not found in {self.department} department"
    
    def list_employees(self):
        if not self.employees:
            return f"No employees in {self.department} department"
        
        result = f"Employees in {self.department} department:\n"
        for emp in self.employees:
            result += f"- {emp.name}\n"
        return result
    
    def __str__(self):
        return f"Manager {self.employee_id}: {self.name}, Department: {self.department}, Salary: ${self.salary}"

class Developer(Employee):
    def __init__(self, employee_id, name, salary, programming_language):
        super().__init__(employee_id, name, salary)
        self.programming_language = programming_language
    
    def code(self):
        return f"{self.name} is coding in {self.programming_language}"
    
    def __str__(self):
        return f"Developer {self.employee_id}: {self.name}, Language: {self.programming_language}, Salary: ${self.salary}"

# Create employees
manager = Manager("M001", "Alice", 80000, "Engineering")
dev1 = Developer("D001", "Bob", 60000, "Python")
dev2 = Developer("D002", "Charlie", 65000, "Java")

# Use employee management system
print(manager)  # Output: Manager M001: Alice, Department: Engineering, Salary: $80000
print(manager.add_employee(dev1))  # Output: Added Bob to Engineering department
print(manager.add_employee(dev2))  # Output: Added Charlie to Engineering department
print(manager.list_employees())  # Output: Employees in Engineering department: - Bob - Charlie
print(dev1.code())  # Output: Bob is coding in Python
print(manager.remove_employee(dev1))  # Output: Removed Bob from Engineering department
print(manager.list_employees())  # Output: Employees in Engineering department: - Charlie
```

## Conclusion

Object-Oriented Programming in Python provides powerful tools for organizing and structuring your code. By using classes, objects, inheritance, and polymorphism, you can create more maintainable, reusable, and scalable applications.

Key takeaways:
- Lambda functions provide a concise way to create small, anonymous functions
- Lists (arrays) in Python are versatile data structures for storing collections of items
- Classes define blueprints for objects, encapsulating data and behavior
- Inheritance allows for code reuse and establishing relationships between classes
- Polymorphism enables flexibility and extensibility in your code

In the next part of our class, we'll apply these concepts to build a real-life project: an Online Bookstore Management System.
