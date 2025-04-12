# Python OOP Lecture Materials

This package contains all materials for teaching Object-Oriented Programming in Python, including:

## Contents

1. **Lecture Material**
   - Comprehensive markdown document covering:
     - Lambda Functions
     - Arrays (Lists in Python)
     - Classes and Objects
     - Inheritance
     - Polymorphism
     - Practical Examples

2. **PowerPoint Presentation**
   - Colorful slides with examples for classroom teaching
   - Covers all topics from the lecture material
   - Designed to be engaging for beginners

3. **Online Bookstore Management System Project**
   - Complete working project demonstrating OOP concepts
   - Features:
     - User Authentication
     - Inventory Management
     - Shopping Cart Functionality
     - Order Processing
   - Well-documented code with comments

## How to Use These Materials

### For Teaching:
1. Review the markdown lecture material for comprehensive content
2. Use the PowerPoint presentation for classroom instruction
3. Demonstrate the Online Bookstore project to show practical application

### For the Project Demo:
1. Navigate to the project directory: `cd project/online_bookstore`
2. Run the application: `python main.py`
3. Sample login credentials:
   - Admin: username=admin, password=admin123
   - Customer: username=customer, password=customer123

## Project Structure

```
python_oop_lecture/
├── lecture_material/
│   └── python_oop_lecture.md
├── presentation/
│   ├── Python_OOP_Lecture.pptx
│   └── create_presentation.py
└── project/
    └── online_bookstore/
        ├── models/
        │   ├── book.py
        │   ├── user.py
        │   └── inventory.py
        ├── controllers/
        │   ├── auth_controller.py
        │   ├── book_controller.py
        │   └── cart_controller.py
        ├── views/
        │   └── cli.py
        ├── data/
        ├── utils/
        ├── main.py
        └── README.md
```

## Notes for Instructors

- The lecture is designed for beginners with basic Python knowledge
- The project demonstrates all OOP concepts covered in the lecture
- Feel free to modify or extend these materials to suit your specific teaching needs
