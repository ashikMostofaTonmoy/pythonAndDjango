"""
Student Grading System

This program allows users to manage student grades through a command-line interface.
Features include:
- Adding students
- Recording grades
- Calculating averages
- Generating reports

This is a practical example of using functions, loops, and data structures in Python.
"""

# Import modules
import os
import csv
import datetime
from statistics import mean

# Global variables
# Dictionary to store student data: {student_id: {'name': name, 'grades': {subject: [grades]}}}
students = {}


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_header(title):
    """Display a formatted header."""
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50 + "\n")


def get_valid_input(prompt, validation_func, error_message):
    """
    Get user input with validation.

    Args:
        prompt: The input prompt to display
        validation_func: Function to validate input
        error_message: Message to display if validation fails

    Returns:
        Valid user input
    """
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print(error_message)


def is_valid_student_id(student_id):
    """Check if student ID is valid (non-empty string)."""
    return bool(student_id.strip())


def is_valid_name(name):
    """Check if name is valid (non-empty string)."""
    return bool(name.strip())


def is_valid_subject(subject):
    """Check if subject is valid (non-empty string)."""
    return bool(subject.strip())


def is_valid_grade(grade):
    """Check if grade is valid (number between 0 and 100)."""
    try:
        grade_value = float(grade)
        return 0 <= grade_value <= 100
    except ValueError:
        return False


def add_student():
    """Add a new student to the system."""
    display_header("Add New Student")

    # Get student ID
    while True:
        student_id = get_valid_input(
            "Enter student ID: ", is_valid_student_id, "Student ID cannot be empty.")
        if student_id in students:
            print(
                f"Student ID '{student_id}' already exists. Please use a different ID.")
        else:
            break

    # Get student name
    name = get_valid_input("Enter student name: ",
                           is_valid_name, "Name cannot be empty.")

    # Add student to dictionary
    students[student_id] = {
        'name': name,
        'grades': {}
    }

    print(
        f"\nStudent '{name}' with ID '{student_id}' has been added successfully!")
    input("\nPress Enter to continue...")


def record_grade():
    """Record grades for a student."""
    display_header("Record Grades")

    if not students:
        print("No students in the system. Please add students first.")
        input("\nPress Enter to continue...")
        return

    # Display available students
    print("Available Students:")
    for student_id, data in students.items():
        print(f"ID: {student_id}, Name: {data['name']}")

    # Get student ID
    while True:
        student_id = get_valid_input(
            "\nEnter student ID: ", is_valid_student_id, "Student ID cannot be empty.")
        if student_id not in students:
            print(f"Student ID '{student_id}' not found. Please try again.")
        else:
            break

    # Get subject
    subject = get_valid_input(
        "Enter subject: ", is_valid_subject, "Subject cannot be empty.")

    # Initialize subject in grades dictionary if it doesn't exist
    if subject not in students[student_id]['grades']:
        students[student_id]['grades'][subject] = []

    # Get grade
    grade = float(get_valid_input("Enter grade (0-100): ",
                  is_valid_grade, "Grade must be a number between 0 and 100."))

    # Add grade to student's subject
    students[student_id]['grades'][subject].append(grade)

    print(
        f"\nGrade {grade} for {subject} has been recorded for {students[student_id]['name']}.")
    input("\nPress Enter to continue...")


def view_student_grades():
    """View grades for a specific student."""
    display_header("View Student Grades")

    if not students:
        print("No students in the system. Please add students first.")
        input("\nPress Enter to continue...")
        return

    # Display available students
    print("Available Students:")
    for student_id, data in students.items():
        print(f"ID: {student_id}, Name: {data['name']}")

    # Get student ID
    while True:
        student_id = get_valid_input(
            "\nEnter student ID: ", is_valid_student_id, "Student ID cannot be empty.")
        if student_id not in students:
            print(f"Student ID '{student_id}' not found. Please try again.")
        else:
            break

    student_data = students[student_id]
    name = student_data['name']
    grades = student_data['grades']

    print(f"\nGrades for {name} (ID: {student_id}):")

    if not grades:
        print("No grades recorded yet.")
    else:
        print("\n{:<15} {:<10} {:<10} {:<10}".format(
            "Subject", "Average", "Highest", "Lowest"))
        print("-" * 45)

        overall_grades = []

        for subject, subject_grades in grades.items():
            if subject_grades:
                avg = mean(subject_grades)
                highest = max(subject_grades)
                lowest = min(subject_grades)
                overall_grades.extend(subject_grades)

                print("{:<15} {:<10.2f} {:<10.2f} {:<10.2f}".format(
                    subject, avg, highest, lowest))
                print(
                    f"  All grades: {', '.join(str(g) for g in subject_grades)}")

        if overall_grades:
            overall_avg = mean(overall_grades)
            print("\nOverall Average: {:.2f}".format(overall_avg))
            print("Letter Grade: {}".format(get_letter_grade(overall_avg)))

    input("\nPress Enter to continue...")


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


def class_summary():
    """Generate a summary report for all students."""
    display_header("Class Summary Report")

    if not students:
        print("No students in the system. Please add students first.")
        input("\nPress Enter to continue...")
        return

    # Calculate class statistics
    all_grades = []
    student_averages = {}

    for student_id, data in students.items():
        student_grades = []
        for subject_grades in data['grades'].values():
            student_grades.extend(subject_grades)

        if student_grades:
            avg = mean(student_grades)
            student_averages[student_id] = avg
            all_grades.extend(student_grades)

    # Display class statistics
    if all_grades:
        class_avg = mean(all_grades)
        highest_avg = max(student_averages.values()) if student_averages else 0
        lowest_avg = min(student_averages.values()) if student_averages else 0

        print("Class Statistics:")
        print(f"Number of Students: {len(students)}")
        print(f"Class Average: {class_avg:.2f}")
        print(f"Highest Student Average: {highest_avg:.2f}")
        print(f"Lowest Student Average: {lowest_avg:.2f}")

        # Find top performers
        print("\nTop Performers:")
        sorted_students = sorted(
            student_averages.items(), key=lambda x: x[1], reverse=True)

        for i, (student_id, avg) in enumerate(sorted_students[:3], 1):
            name = students[student_id]['name']
            print(
                f"{i}. {name} (ID: {student_id}) - Average: {avg:.2f}, Grade: {get_letter_grade(avg)}")

        # Display all students
        print("\nAll Students:")
        print("\n{:<5} {:<15} {:<10} {:<10}".format(
            "ID", "Name", "Average", "Grade"))
        print("-" * 40)

        for student_id, data in students.items():
            name = data['name']
            student_grades = []

            for subject_grades in data['grades'].values():
                student_grades.extend(subject_grades)

            if student_grades:
                avg = mean(student_grades)
                grade = get_letter_grade(avg)
                print("{:<5} {:<15} {:<10.2f} {:<10}".format(
                    student_id, name, avg, grade))
            else:
                print("{:<5} {:<15} {:<10} {:<10}".format(
                    student_id, name, "N/A", "N/A"))
    else:
        print("No grades recorded yet for any student.")

    input("\nPress Enter to continue...")


def subject_summary():
    """Generate a summary report by subject."""
    display_header("Subject Summary Report")

    if not students:
        print("No students in the system. Please add students first.")
        input("\nPress Enter to continue...")
        return

    # Collect all subjects
    all_subjects = set()
    for data in students.values():
        all_subjects.update(data['grades'].keys())

    if not all_subjects:
        print("No grades recorded yet for any subject.")
        input("\nPress Enter to continue...")
        return

    # Display available subjects
    print("Available Subjects:")
    for i, subject in enumerate(sorted(all_subjects), 1):
        print(f"{i}. {subject}")

    # Get subject choice
    while True:
        subject_choice = input("\nEnter subject name: ")
        if subject_choice in all_subjects:
            break
        print(f"Subject '{subject_choice}' not found. Please try again.")

    # Collect grades for the chosen subject
    subject_grades = {}
    for student_id, data in students.items():
        if subject_choice in data['grades'] and data['grades'][subject_choice]:
            subject_grades[student_id] = mean(data['grades'][subject_choice])

    # Display subject statistics
    print(f"\nSummary for {subject_choice}:")

    if subject_grades:
        subject_avg = mean(subject_grades.values())
        highest_avg = max(subject_grades.values())
        lowest_avg = min(subject_grades.values())

        print(f"Number of Students: {len(subject_grades)}")
        print(f"Subject Average: {subject_avg:.2f}")
        print(f"Highest Average: {highest_avg:.2f}")
        print(f"Lowest Average: {lowest_avg:.2f}")

        # Display student performance in this subject
        print("\nStudent Performance:")
        print("\n{:<5} {:<15} {:<10} {:<10}".format(
            "ID", "Name", "Average", "Grade"))
        print("-" * 40)

        sorted_students = sorted(
            subject_grades.items(), key=lambda x: x[1], reverse=True)

        for student_id, avg in sorted_students:
            name = students[student_id]['name']
            grade = get_letter_grade(avg)
            print("{:<5} {:<15} {:<10.2f} {:<10}".format(
                student_id, name, avg, grade))
    else:
        print(f"No grades recorded yet for {subject_choice}.")

    input("\nPress Enter to continue...")


def export_data():
    """Export student data to CSV files."""
    display_header("Export Data")

    if not students:
        print("No students in the system. Please add students first.")
        input("\nPress Enter to continue...")
        return

    # Create timestamp for filenames
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Export student list
    students_filename = f"students_{timestamp}.csv"
    with open(students_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Name"])

        for student_id, data in students.items():
            writer.writerow([student_id, data['name']])

    # Export grades
    grades_filename = f"grades_{timestamp}.csv"
    with open(grades_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Name", "Subject", "Grade"])

        for student_id, data in students.items():
            name = data['name']
            for subject, grades in data['grades'].items():
                for grade in grades:
                    writer.writerow([student_id, name, subject, grade])

    # Export summary
    summary_filename = f"summary_{timestamp}.csv"
    with open(summary_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Student ID", "Name", "Overall Average", "Letter Grade"])

        for student_id, data in students.items():
            name = data['name']
            all_grades = []

            for subject_grades in data['grades'].values():
                all_grades.extend(subject_grades)

            if all_grades:
                avg = mean(all_grades)
                letter_grade = get_letter_grade(avg)
                writer.writerow([student_id, name, f"{avg:.2f}", letter_grade])
            else:
                writer.writerow([student_id, name, "N/A", "N/A"])

    print(f"Data exported successfully to the following files:")
    print(f"1. {students_filename} - Student list")
    print(f"2. {grades_filename} - All grades")
    print(f"3. {summary_filename} - Summary report")

    input("\nPress Enter to continue...")


def import_data():
    """Import student data from CSV files."""
    display_header("Import Data")

    # Get filename
    filename = input("Enter the path to the CSV file: ")

    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        input("\nPress Enter to continue...")
        return

    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header row

            if header == ["Student ID", "Name"]:
                # Importing student list
                for row in reader:
                    if len(row) >= 2:
                        student_id, name = row[0], row[1]
                        if student_id not in students:
                            students[student_id] = {'name': name, 'grades': {}}
                print("Student list imported successfully.")

            elif header == ["Student ID", "Name", "Subject", "Grade"]:
                # Importing grades
                for row in reader:
                    if len(row) >= 4:
                        student_id, name, subject, grade = row[0], row[1], row[2], row[3]

                        # Add student if not exists
                        if student_id not in students:
                            students[student_id] = {'name': name, 'grades': {}}

                        # Initialize subject if not exists
                        if subject not in students[student_id]['grades']:
                            students[student_id]['grades'][subject] = []

                        # Add grade
                        try:
                            grade_value = float(grade)
                            students[student_id]['grades'][subject].append(
                                grade_value)
                        except ValueError:
                            print(
                                f"Invalid grade value '{grade}' for student {name}. Skipping.")

                print("Grades imported successfully.")
            else:
                print("Unrecognized CSV format. Please use a valid export file.")
    except Exception as e:
        print(f"Error importing data: {e}")

    input("\nPress Enter to continue...")


def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        clear_screen()
        display_header("Student Grading System")

        print("1. Add Student")
        print("2. Record Grade")
        print("3. View Student Grades")
        print("4. Class Summary Report")
        print("5. Subject Summary Report")
        print("6. Export Data")
        print("7. Import Data")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            record_grade()
        elif choice == '3':
            view_student_grades()
        elif choice == '4':
            class_summary()
        elif choice == '5':
            subject_summary()
        elif choice == '6':
            export_data()
        elif choice == '7':
            import_data()
        elif choice == '8':
            clear_screen()
            print("Thank you for using the Student Grading System!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")


def initialize_sample_data():
    """Initialize the system with sample data for demonstration."""
    # Add sample students
    students["S001"] = {
        'name': 'John Smith',
        'grades': {
            'Math': [85, 90, 78],
            'Science': [92, 88, 95],
            'English': [75, 82, 80]
        }
    }

    students["S002"] = {
        'name': 'Emily Johnson',
        'grades': {
            'Math': [95, 92, 98],
            'Science': [90, 85, 92],
            'English': [88, 92, 90]
        }
    }

    students["S003"] = {
        'name': 'Michael Brown',
        'grades': {
            'Math': [65, 70, 72],
            'Science': [68, 72, 75],
            'English': [70, 75, 78]
        }
    }

    students["S004"] = {
        'name': 'Sarah Davis',
        'grades': {
            'Math': [78, 82, 80],
            'Science': [85, 80, 83],
            'English': [92, 95, 90]
        }
    }

    print("Sample data initialized successfully!")


if __name__ == "__main__":
    # Ask if user wants to load sample data
    clear_screen()
    display_header("Student Grading System")

    load_sample = input("Would you like to load sample data? (y/n): ")
    if load_sample.lower() == 'y':
        initialize_sample_data()

    main_menu()
