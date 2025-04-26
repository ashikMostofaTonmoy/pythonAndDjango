# Python Day 5: Exercises

## File Handling Exercises

### Exercise 1: Basic File Operations
Create a Python script that:
1. Creates a new text file named "notes.txt"
2. Writes at least three lines of text to it
3. Closes the file
4. Opens the file again and reads the content
5. Prints the content to the console

### Exercise 2: CSV File Manipulation
1. Create a CSV file named "students.csv" with the following data:
   ```
   ID,Name,Age,Grade
   101,John,18,A
   102,Mary,17,B
   103,Bob,19,A
   104,Sarah,18,C
   ```
2. Write a Python script that:
   - Reads the CSV file
   - Adds two more students
   - Calculates the average age
   - Counts how many students have each grade
   - Writes the updated data back to the CSV file

### Exercise 3: JSON Configuration
1. Create a Python script that:
   - Creates a configuration dictionary with settings for an application (e.g., username, theme, language, etc.)
   - Saves this configuration to a JSON file
   - Loads the configuration
   - Modifies one setting
   - Saves it again

### Exercise 4: File Finder
Create a Python script that searches for all files with a specific extension (e.g., ".txt") in a given directory and its subdirectories, and prints their paths.

## NumPy Exercises

### Exercise 5: Array Creation and Manipulation
1. Create a 3x3 NumPy array of random integers between 1 and 10
2. Find the minimum, maximum, and average values
3. Extract the diagonal elements
4. Reverse the array horizontally and vertically

### Exercise 6: Mathematical Operations
1. Create two 4x4 NumPy arrays:
   - Array A with values from 1 to 16 (reshaped to 4x4)
   - Array B with random values between 0 and 1
2. Perform element-wise multiplication
3. Calculate the dot product of A and B
4. Calculate the determinant of A
5. Find the eigenvalues of A

### Exercise 7: Array Filtering
1. Create a 1D NumPy array of 20 random integers between 1 and 100
2. Create a new array containing only the elements that are:
   - Even numbers
   - Greater than 50
   - Divisible by 3
3. Replace all prime numbers in the array with -1

## Pandas Exercises

### Exercise 8: DataFrame Creation and Basic Operations
1. Create a DataFrame with data about 5 movies (columns: title, director, year, rating)
2. Sort the DataFrame by rating (highest first)
3. Filter to show only movies with a rating above 8
4. Add a new column "watched" with Boolean values
5. Display summary statistics for the numerical columns

### Exercise 9: Data Analysis
Using the following dataset:
```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'HR', 'IT'],
    'Salary': [60000, 80000, 75000, 90000, 65000, 85000, 70000, 95000],
    'Experience': [3, 5, 4, 7, 2, 6, 4, 8],
    'Performance': ['Good', 'Excellent', 'Good', 'Excellent', 'Average', 'Good', 'Average', 'Excellent']
}
```

Create a script that:
1. Creates a DataFrame from this data
2. Calculates the average salary per department
3. Finds the highest-paid employee per department
4. Creates a new column "Bonus" that is 10% of salary for "Excellent" performers, 5% for "Good", and 2% for "Average"
5. Creates a pivot table showing average salary and experience by department and performance

### Exercise 10: Data Cleaning and Transformation
Given the following (intentionally messy) data:
```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eve'],
    'Age': [25, 30, None, 40, 35],
    'Salary': ['50000', '60,000', '75000.5', '90000', None],
    'Join_Date': ['2020-01-15', '2019/05/20', '2018.10.10', None, '2021-03-25']
}
```

Create a script that:
1. Creates a DataFrame from this data
2. Handles missing values appropriately (fill or drop)
3. Converts salary to a numeric type
4. Standardizes the date format in Join_Date
5. Adds a new column showing tenure in years based on Join_Date

## Integrated Project Exercise

### Exercise 11: Stock Portfolio Tracker
Create a Stock Portfolio Tracker application that:

1. Keeps track of stocks a user has purchased (stock symbol, purchase price, quantity, purchase date)
2. Saves the portfolio data to a CSV file
3. Loads the portfolio data when the program starts
4. Allows the user to:
   - Add new stock purchases
   - View the current portfolio
   - Calculate the total value of the portfolio (using any arbitrary current price)
   - Generate a report showing profit/loss for each stock

Use file handling for data persistence, NumPy for calculations, and Pandas for data analysis and reporting. 