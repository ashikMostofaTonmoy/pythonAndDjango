"""
README for Online Bookstore Management System

This project demonstrates Object-Oriented Programming concepts in Python through a practical
implementation of an Online Bookstore Management System.

## Project Structure

- `models/`: Contains the data models
  - `book.py`: Book class representing books in the inventory
  - `user.py`: User class with authentication and cart functionality
  - `inventory.py`: Inventory class for managing book collections

- `controllers/`: Contains the business logic
  - `auth_controller.py`: Handles user authentication and management
  - `book_controller.py`: Manages book and inventory operations
  - `cart_controller.py`: Handles shopping cart operations

- `views/`: Contains the user interface
  - `cli.py`: Command Line Interface for interacting with the system

- `main.py`: Entry point for the application

## Features

1. **User Authentication**
   - User registration and login
   - Role-based access control (admin/customer)

2. **Inventory Management**
   - Add, update, and remove books
   - Search books by title, author, or genre
   - Track stock levels and inventory value

3. **Shopping Cart**
   - Add books to cart
   - Update quantities or remove items
   - Calculate total price

4. **Order Processing**
   - Checkout functionality
   - Order history tracking

## OOP Concepts Demonstrated

- **Classes and Objects**: Book, User, Inventory classes
- **Encapsulation**: Data and methods are bundled within classes
- **Inheritance**: Not explicitly used but structure allows for it
- **Polymorphism**: Different controllers interact with models in consistent ways
- **Abstraction**: Complex operations are hidden behind simple interfaces

## How to Run

1. Navigate to the project directory
2. Run the main application:
   ```
   python main.py
   ```

3. Sample credentials:
   - Admin: username=admin, password=admin123
   - Customer: username=customer, password=customer123

## Educational Purpose

This project is designed as a teaching tool to demonstrate OOP concepts in Python.
It includes comprehensive documentation and follows best practices for code organization
and structure.
"""
