# Personal Budget Tracker

A command-line application for tracking personal finances, built with Python's file handling capabilities.

## Features

- Record income and expenses with dates, categories, and descriptions
- Save transactions to a CSV file for persistence
- Generate monthly reports with income, expenses, and balance
- View spending by category
- Search transactions
- Calculate current balance

## Requirements

- Python 3.6 or higher

## Usage

1. Run the application:
   ```bash
   python budget_tracker.py
   ```

2. Follow the on-screen menu to:
   - Add income or expenses
   - View all transactions
   - Search for specific transactions
   - Generate monthly reports
   - View your current balance

## How It Works

### Data Storage
The application stores all transactions in a CSV file named `transactions.csv` with the following structure:
- Date (YYYY-MM-DD)
- Type (Income/Expense)
- Category (e.g., Salary, Groceries, Rent)
- Amount (numeric value)
- Description (text description)

### File Operations
- The application demonstrates various file operations:
  - Creating a new file if it doesn't exist
  - Reading data from a CSV file
  - Writing data to a CSV file
  - Handling file exceptions

### Classes and Methods
The main `BudgetTracker` class provides methods for:
- Loading and saving transactions from/to the CSV file
- Adding new transactions
- Searching and filtering transactions
- Generating reports and statistics

## Learning Objectives

This project demonstrates:
1. Working with CSV files in Python
2. File reading, writing, and error handling
3. Data manipulation and formatting
4. Command-line user interface design
5. Object-oriented programming
6. Basic financial calculations

## Extending the Project

Some ideas to extend the project:
- Add data visualization using matplotlib
- Implement budget goals and limits
- Create recurring transactions
- Export reports to Excel or PDF
- Build a web-based interface using a Python web framework
- Add password protection for sensitive financial data 