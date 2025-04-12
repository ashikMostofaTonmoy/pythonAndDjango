# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"


print("Welcome to Student Grading System!")

# List of Students (Dictionary for each student)
students = []

# Input total students
total_students = int(input("Enter number of students: "))

# For Loop to input student data
for i in range(total_students):
    print(f"\nEnter data for Student {i+1}")
    name = input("Name: ")
    marks = int(input("Marks (out of 100): "))

    # Creating student dictionary
    student = {
        "name": name,
        "marks": marks,
        "grade": calculate_grade(marks)
    }

    # Adding student to list
    students.append(student)

print("\n--- Student Results ---")
# While Loop to display all students
index = 0
while index < len(students):
    student = students[index]
    print(
        f"Name: {student['name']}, Marks: {student['marks']}, Grade: {student['grade']}")
    index += 1

# Using Set for unique grades
unique_grades = set(student["grade"] for student in students)

print("\nUnique Grades in Class:", unique_grades)
