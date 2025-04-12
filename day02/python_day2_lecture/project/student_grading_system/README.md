# Student Grading System

This project demonstrates the practical application of Python functions, loops, and data structures through a comprehensive Student Grading System.

## Features

- **Add Students**: Register new students with unique IDs
- **Record Grades**: Enter grades for students in various subjects
- **View Student Grades**: See detailed grade information for individual students
- **Class Summary Report**: Generate overall class performance statistics
- **Subject Summary Report**: Analyze performance in specific subjects
- **Export/Import Data**: Save and load data using CSV files

## How It Works

The Student Grading System uses:
- **Functions** to organize code into reusable blocks
- **Loops** to process collections of data
- **Data Structures** (dictionaries, lists) to store and manage student information

## Data Structure

The program uses a nested dictionary structure to store student data:
```python
students = {
    "student_id": {
        'name': "Student Name",
        'grades': {
            'Subject1': [grade1, grade2, grade3],
            'Subject2': [grade1, grade2, grade3]
        }
    }
}
```

## Functions Overview

- `add_student()`: Adds a new student to the system
- `record_grade()`: Records grades for a specific student and subject
- `view_student_grades()`: Displays grades for a specific student
- `class_summary()`: Generates a report of all students' performance
- `subject_summary()`: Analyzes performance in a specific subject
- `export_data()`: Saves student data to CSV files
- `import_data()`: Loads student data from CSV files

## Running the Program

1. Execute the script: `python student_grading.py`
2. Choose whether to load sample data
3. Navigate through the menu to use different features

## Educational Value

This project demonstrates:
- Practical application of functions with parameters and return values
- Use of while and for loops for data processing
- Implementation of dictionaries and lists for data management
- File I/O operations with CSV files
- Input validation and error handling
- Command-line user interface design

## Sample Data

The program includes sample data for demonstration purposes, featuring four students with grades in Math, Science, and English.

## Requirements

- Python 3.x
- Standard library modules: os, csv, datetime, statistics
