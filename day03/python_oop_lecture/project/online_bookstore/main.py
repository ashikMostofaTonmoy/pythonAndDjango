"""
Main Application for Online Bookstore Management System

This module initializes and runs the Online Bookstore Management System.
"""

from models.book import Book
from models.user import User
from models.inventory import Inventory
from controllers.auth_controller import AuthController
from controllers.book_controller import BookController
from controllers.cart_controller import CartController
from views.cli import CLI

def initialize_sample_data():
    """
    Initialize sample data for demonstration purposes.
    
    Returns:
        tuple: (auth_controller, book_controller, cart_controller)
    """
    # Create controllers
    auth_controller = AuthController()
    inventory = Inventory()
    book_controller = BookController(inventory, auth_controller)
    cart_controller = CartController(auth_controller, book_controller)
    
    # Add sample users
    admin = User("U001", "admin", "admin123", "Admin User", "admin@bookstore.com", "123 Admin St", True)
    customer = User("U002", "customer", "customer123", "John Doe", "john@example.com", "456 Customer Ave")
    
    auth_controller.register_user(admin)
    auth_controller.register_user(customer)
    
    # Add sample books
    books = [
        Book("B001", "Python Programming", "John Smith", "978-1-123456-78-9", 29.99, 10, "Programming", "Tech Books Inc", 2022),
        Book("B002", "Data Science Basics", "Jane Doe", "978-1-234567-89-0", 34.99, 8, "Programming", "Data Press", 2021),
        Book("B003", "Web Development", "Bob Johnson", "978-2-345678-90-1", 27.99, 15, "Programming", "Web Books", 2023),
        Book("B004", "The Great Novel", "Alice Brown", "978-3-456789-01-2", 19.99, 20, "Fiction", "Fiction House", 2020),
        Book("B005", "History of Computing", "David Wilson", "978-4-567890-12-3", 24.99, 5, "History", "History Press", 2019),
        Book("B006", "Artificial Intelligence", "Emily Clark", "978-5-678901-23-4", 39.99, 7, "Programming", "AI Publishers", 2022),
        Book("B007", "Database Design", "Michael Lee", "978-6-789012-34-5", 32.99, 12, "Programming", "Tech Books Inc", 2021),
        Book("B008", "Network Security", "Sarah Miller", "978-7-890123-45-6", 29.99, 9, "Security", "Security Press", 2023),
        Book("B009", "Cloud Computing", "James Wilson", "978-8-901234-56-7", 36.99, 6, "Programming", "Cloud Books", 2022),
        Book("B010", "Machine Learning", "Jennifer Taylor", "978-9-012345-67-8", 42.99, 4, "Programming", "AI Publishers", 2023)
    ]
    
    for book in books:
        book_controller.add_book(book)
    
    return auth_controller, book_controller, cart_controller

def main():
    """
    Main function to run the application.
    """
    print("Initializing Online Bookstore Management System...")
    auth_controller, book_controller, cart_controller = initialize_sample_data()
    
    # Create and run CLI
    cli = CLI(auth_controller, book_controller, cart_controller)
    cli.run()

if __name__ == "__main__":
    main()
