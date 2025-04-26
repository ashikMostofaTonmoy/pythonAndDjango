# Python Day 5: File Handling, NumPy, and Pandas

## 1. Python File Handling

File handling is crucial for working with external data, storing application state, logging, and more. Python provides simple and consistent interfaces for file operations.

### 1.1 Opening and Closing Files

```python
# Basic file opening - always use with statement when possible
with open('filename.txt', 'r') as file:
    # File operations here
    pass  # File is automatically closed when the block ends

# Alternative way - requires manual closing
file = open('filename.txt', 'r')
# File operations here
file.close()  # Must explicitly close the file
```

### 1.2 File Modes

- `'r'` - Read (default). Opens file for reading.
- `'w'` - Write. Creates a new file or truncates an existing file.
- `'a'` - Append. Opens for writing, appending to the end of file.
- `'x'` - Exclusive creation. Fails if file already exists.
- `'b'` - Binary mode (can be combined with other modes).
- `'t'` - Text mode (default, can be combined with other modes).
- `'+'` - Update mode (reading and writing).

Examples:
```python
# Text mode examples
with open('data.txt', 'r') as f:  # Read text
    pass
with open('output.txt', 'w') as f:  # Write text (create/truncate)
    pass
with open('log.txt', 'a') as f:  # Append text
    pass

# Binary mode examples
with open('image.jpg', 'rb') as f:  # Read binary
    pass
with open('backup.zip', 'wb') as f:  # Write binary
    pass
```

### 1.3 Reading from Files

```python
# Reading the entire file at once
with open('data.txt', 'r') as file:
    content = file.read()  # Reads the entire file
    print(content)

# Reading line by line
with open('data.txt', 'r') as file:
    for line in file:  # Efficient way to read large files
        print(line.strip())  # strip() removes the newline character

# Reading all lines into a list
with open('data.txt', 'r') as file:
    lines = file.readlines()  # Returns a list where each element is a line
    for line in lines:
        print(line.strip())

# Reading a specific number of characters
with open('data.txt', 'r') as file:
    chunk = file.read(10)  # Reads the first 10 characters
    print(chunk)
```

### 1.4 Writing to Files

```python
# Writing a string to a file
with open('output.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")

# Writing multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as file:
    file.writelines(lines)  # Note: writelines doesn't add newlines

# Appending to a file
with open('log.txt', 'a') as file:
    file.write("New log entry\n")
```

### 1.5 Deleting Files

To delete files, you need to use the `os` module:

```python
import os

# Check if file exists before deleting
if os.path.exists('file_to_delete.txt'):
    os.remove('file_to_delete.txt')
    print("File deleted successfully")
else:
    print("The file does not exist")

# Delete entire directory
import shutil
shutil.rmtree('directory_to_delete')  # Be careful! This deletes everything in the directory
```

### 1.6 Working with CSV Files

CSV (Comma-Separated Values) is a common format for storing tabular data:

```python
import csv

# Reading CSV
with open('data.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of values

# Writing CSV
data = [
    ['Name', 'Age', 'Country'],
    ['Alice', '25', 'USA'],
    ['Bob', '30', 'Canada'],
    ['Charlie', '35', 'UK']
]
with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write all rows at once

# Using CSV with dictionaries
with open('data.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)  # First row is treated as header/column names
    for row in reader:
        print(row['Name'], row['Age'])  # Access by column name
```

### 1.7 Working with JSON Files

JSON (JavaScript Object Notation) is a lightweight data format that's easy for humans to read and write:

```python
import json

# Writing JSON
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'languages': ['Python', 'JavaScript', 'SQL'],
    'is_employee': True
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # indent makes the file human-readable

# Reading JSON
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data['name'])  # Accessing values
    print(loaded_data['languages'])
```

## 2. NumPy Library

NumPy (Numerical Python) is a fundamental package for scientific computing in Python. It provides support for arrays, matrices, and many mathematical functions.

### 2.1 Installing NumPy

```bash
pip install numpy
```

### 2.2 Creating Arrays

```python
import numpy as np

# Creating arrays from lists
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# Creating 2D arrays
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
# [[1 2 3]
#  [4 5 6]]

# Creating arrays with specific values
zeros = np.zeros((3, 4))  # 3x4 array of zeros
ones = np.ones((2, 3))    # 2x3 array of ones
full = np.full((2, 2), 7)  # 2x2 array filled with 7

# Creating sequences
rng = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
lin = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1

# Random arrays
random_arr = np.random.random((2, 2))  # 2x2 array of random values [0,1)
```

### 2.3 Array Attributes and Methods

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Array attributes
print(arr.shape)      # (2, 3) - dimensions
print(arr.ndim)       # 2 - number of dimensions
print(arr.size)       # 6 - total number of elements
print(arr.dtype)      # int64 - data type of elements

# Reshaping arrays
reshaped = arr.reshape(3, 2)  # Reshape to 3x2
print(reshaped)
# [[1 2]
#  [3 4]
#  [5 6]]

# Flattening arrays
flattened = arr.flatten()  # Convert to 1D array
print(flattened)  # [1 2 3 4 5 6]
```

### 2.4 Array Operations

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
print(a + b)  # [5 7 9]
print(a - b)  # [-3 -3 -3]
print(a * b)  # [4 10 18]
print(a / b)  # [0.25 0.4 0.5]

# Broadcasting
print(a + 10)  # [11 12 13]

# Matrix multiplication
c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])
print(np.dot(c, d))  # Matrix product
# [[19 22]
#  [43 50]]

# Universal functions
print(np.sqrt(a))    # Square root of each element
print(np.exp(a))     # e^x for each element
print(np.sin(a))     # Sine of each element
```

### 2.5 Array Indexing and Slicing

```python
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Indexing
print(arr[0, 0])  # 1 - first element
print(arr[2, 3])  # 12 - last element

# Slicing
print(arr[0:2, 1:3])  # Get a 2x2 sub-array
# [[2 3]
#  [6 7]]

# Boolean indexing
mask = arr > 5
print(mask)  # Boolean array
print(arr[mask])  # Array of elements where condition is True

# Fancy indexing
row_indices = [0, 1, 2]
col_indices = [3, 2, 1]
print(arr[row_indices, col_indices])  # [4 7 10]
```

## 3. Pandas Library

Pandas is a powerful data manipulation and analysis library for Python, built on top of NumPy.

### 3.1 Installing Pandas

```bash
pip install pandas
```

### 3.2 Creating DataFrames

```python
import pandas as pd
import numpy as np

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Boston', 'Chicago', 'Denver']
}
df = pd.DataFrame(data)
print(df)
#       Name  Age      City
# 0    Alice   25  New York
# 1      Bob   30    Boston
# 2  Charlie   35   Chicago
# 3    David   40    Denver

# Creating a DataFrame from a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df2 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df2)
#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

# Creating a DataFrame from a CSV file
df3 = pd.read_csv('data.csv')
```

### 3.3 Examining DataFrames

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000],
    'Department': ['HR', 'IT', 'Finance', 'IT']
})

# Basic DataFrame information
print(df.shape)       # (4, 4) - dimensions
print(df.dtypes)      # Data types of columns
print(df.columns)     # Column names
print(df.index)       # Row indices

# Viewing data
print(df.head(2))     # First 2 rows
print(df.tail(2))     # Last 2 rows
print(df.sample(2))   # Random 2 rows

# Summary statistics
print(df.describe())  # Statistical summary of numerical columns
```

### 3.4 Selecting Data

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000],
    'Department': ['HR', 'IT', 'Finance', 'IT']
})

# Selecting columns
print(df['Name'])           # Single column as Series
print(df[['Name', 'Age']])  # Multiple columns as DataFrame

# Selecting rows by position
print(df.iloc[0])      # First row
print(df.iloc[1:3])    # Second and third rows
print(df.iloc[0, 1])   # Value at row 0, column 1 (Alice's age: 25)

# Selecting rows by label
print(df.loc[0, 'Name'])  # 'Alice'
print(df.loc[0:2, ['Name', 'Department']])  # First 3 rows, specific columns

# Filtering data
print(df[df['Age'] > 30])               # Rows where Age > 30
print(df[df['Department'] == 'IT'])     # Rows where Department is IT
```

### 3.5 Modifying DataFrames

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000],
    'Department': ['HR', 'IT', 'Finance', 'IT']
})

# Adding a new column
df['Experience'] = [1, 2, 5, 10]
df['Bonus'] = df['Salary'] * 0.1  # Calculated column

# Modifying values
df.loc[0, 'Salary'] = 55000  # Change Alice's salary
df['Age'] = df['Age'] + 1    # Increment everyone's age

# Renaming columns
df = df.rename(columns={'Name': 'Employee', 'Salary': 'Annual_Salary'})

# Dropping columns or rows
df_dropped = df.drop(columns=['Bonus'])  # Drop a column
df_dropped_rows = df.drop(index=[1, 3])  # Drop rows with index 1 and 3
```

### 3.6 Data Analysis with Pandas

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 80000, 55000],
    'Age': [25, 30, 35, 40, 28]
})

# Grouping data
dept_group = df.groupby('Department')
print(dept_group.mean())  # Average age and salary by department

# Aggregation
print(dept_group['Salary'].agg(['min', 'max', 'mean', 'count']))

# Pivot tables
pivot = pd.pivot_table(df, values='Salary', index='Department', 
                      aggfunc='mean')
print(pivot)

# Sorting
print(df.sort_values('Salary', ascending=False))  # Sort by salary (high to low)
print(df.sort_values(['Department', 'Age']))      # Sort by department, then age
```

### 3.7 Reading and Writing Data

```python
import pandas as pd

# Reading data
df_csv = pd.read_csv('data.csv')
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df_json = pd.read_json('data.json')
df_sql = pd.read_sql('SELECT * FROM employees', connection)

# Writing data
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
df.to_json('output.json', orient='records')
df.to_sql('employees', connection, if_exists='replace', index=False)
```

## 4. Real-life Project: Personal Budget Tracker

For our final project, we'll create a Personal Budget Tracker that incorporates file operations to persist data.

### Requirements:
1. Record income and expenses with date, amount, category, and description
2. Save all data to a CSV file
3. Load data from the CSV file on startup
4. Generate reports (monthly totals, category-wise spending)
5. Allow searching for specific transactions

### Project Structure:
```
budget_tracker/
├── budget_tracker.py     # Main application
├── transactions.csv      # Data file
└── README.md             # Documentation
```

In the next section, we'll implement the Personal Budget Tracker step by step in the project module. 