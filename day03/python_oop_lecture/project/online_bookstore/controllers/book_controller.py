"""
Book Controller for Online Bookstore Management System

This module defines the BookController class which handles book and inventory operations.
"""

class BookController:
    """
    Handles book and inventory operations.
    
    Attributes:
        inventory (Inventory): Inventory object to manage
        auth_controller (AuthController): Authentication controller for permission checks
    """
    
    def __init__(self, inventory, auth_controller):
        """
        Initialize a new BookController instance.
        
        Args:
            inventory (Inventory): Inventory object to manage
            auth_controller (AuthController): Authentication controller for permission checks
        """
        self.inventory = inventory
        self.auth_controller = auth_controller
    
    def add_book(self, book):
        """
        Add a book to the inventory (admin only).
        
        Args:
            book: Book object to add
            
        Returns:
            bool: True if added successfully, False if not admin or book_id already exists
        """
        if not self.auth_controller.is_admin():
            return False
        
        return self.inventory.add_book(book)
    
    def remove_book(self, book_id):
        """
        Remove a book from the inventory (admin only).
        
        Args:
            book_id (str): ID of book to remove
            
        Returns:
            bool: True if removed, False if not admin or not found
        """
        if not self.auth_controller.is_admin():
            return False
        
        return self.inventory.remove_book(book_id)
    
    def update_book(self, book_id, **kwargs):
        """
        Update book information (admin only).
        
        Args:
            book_id (str): ID of book to update
            **kwargs: Attributes to update
            
        Returns:
            bool: True if updated, False if not admin or not found
        """
        if not self.auth_controller.is_admin():
            return False
        
        return self.inventory.update_book(book_id, **kwargs)
    
    def get_book(self, book_id):
        """
        Get a book by ID.
        
        Args:
            book_id (str): ID of book to get
            
        Returns:
            Book: Book object if found, None otherwise
        """
        return self.inventory.get_book(book_id)
    
    def search_books(self, **kwargs):
        """
        Search for books by various criteria.
        
        Args:
            **kwargs: Search criteria (e.g., title, author, genre)
            
        Returns:
            list: List of matching Book objects
        """
        return self.inventory.search_books(**kwargs)
    
    def get_all_books(self):
        """
        Get all books in the inventory.
        
        Returns:
            list: List of all Book objects
        """
        return self.inventory.get_all_books()
    
    def get_books_by_genre(self, genre):
        """
        Get books by genre.
        
        Args:
            genre (str): Genre to search for
            
        Returns:
            list: List of matching Book objects
        """
        return self.inventory.get_books_by_genre(genre)
    
    def get_books_by_author(self, author):
        """
        Get books by author.
        
        Args:
            author (str): Author to search for
            
        Returns:
            list: List of matching Book objects
        """
        return self.inventory.get_books_by_author(author)
    
    def get_low_stock_books(self, threshold=5):
        """
        Get books with low stock (admin only).
        
        Args:
            threshold (int, optional): Stock threshold. Defaults to 5.
            
        Returns:
            list: List of Book objects with quantity below threshold, empty list if not admin
        """
        if not self.auth_controller.is_admin():
            return []
        
        return self.inventory.get_low_stock_books(threshold)
    
    def total_inventory_value(self):
        """
        Calculate the total value of inventory (admin only).
        
        Returns:
            float: Total value, 0 if not admin
        """
        if not self.auth_controller.is_admin():
            return 0
        
        return self.inventory.total_inventory_value()
