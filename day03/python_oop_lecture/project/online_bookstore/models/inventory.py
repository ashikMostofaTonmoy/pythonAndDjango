"""
Inventory Management for Online Bookstore Management System

This module defines the Inventory class which manages the bookstore inventory.
"""

class Inventory:
    """
    Manages the bookstore inventory.
    
    Attributes:
        books (dict): Dictionary of books with book_id as key and Book object as value
    """
    
    def __init__(self):
        """
        Initialize a new Inventory instance.
        """
        self.books = {}
    
    def add_book(self, book):
        """
        Add a book to the inventory.
        
        Args:
            book: Book object to add
            
        Returns:
            bool: True if added successfully, False if book_id already exists
        """
        if book.book_id in self.books:
            return False
        
        self.books[book.book_id] = book
        return True
    
    def remove_book(self, book_id):
        """
        Remove a book from the inventory.
        
        Args:
            book_id (str): ID of book to remove
            
        Returns:
            bool: True if removed, False if not found
        """
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False
    
    def get_book(self, book_id):
        """
        Get a book by ID.
        
        Args:
            book_id (str): ID of book to get
            
        Returns:
            Book: Book object if found, None otherwise
        """
        return self.books.get(book_id)
    
    def update_book(self, book_id, **kwargs):
        """
        Update book information.
        
        Args:
            book_id (str): ID of book to update
            **kwargs: Attributes to update
            
        Returns:
            bool: True if updated, False if not found
        """
        book = self.get_book(book_id)
        if not book:
            return False
        
        for key, value in kwargs.items():
            if hasattr(book, key):
                setattr(book, key, value)
        
        return True
    
    def search_books(self, **kwargs):
        """
        Search for books by various criteria.
        
        Args:
            **kwargs: Search criteria (e.g., title, author, genre)
            
        Returns:
            list: List of matching Book objects
        """
        results = []
        
        for book in self.books.values():
            match = True
            
            for key, value in kwargs.items():
                if hasattr(book, key):
                    book_value = getattr(book, key)
                    
                    # Case-insensitive string comparison
                    if isinstance(book_value, str) and isinstance(value, str):
                        if value.lower() not in book_value.lower():
                            match = False
                            break
                    # Exact match for non-string values
                    elif book_value != value:
                        match = False
                        break
            
            if match:
                results.append(book)
        
        return results
    
    def get_all_books(self):
        """
        Get all books in the inventory.
        
        Returns:
            list: List of all Book objects
        """
        return list(self.books.values())
    
    def get_books_by_genre(self, genre):
        """
        Get books by genre.
        
        Args:
            genre (str): Genre to search for
            
        Returns:
            list: List of matching Book objects
        """
        return self.search_books(genre=genre)
    
    def get_books_by_author(self, author):
        """
        Get books by author.
        
        Args:
            author (str): Author to search for
            
        Returns:
            list: List of matching Book objects
        """
        return self.search_books(author=author)
    
    def get_low_stock_books(self, threshold=5):
        """
        Get books with low stock.
        
        Args:
            threshold (int, optional): Stock threshold. Defaults to 5.
            
        Returns:
            list: List of Book objects with quantity below threshold
        """
        return [book for book in self.books.values() if book.quantity <= threshold]
    
    def total_inventory_value(self):
        """
        Calculate the total value of inventory.
        
        Returns:
            float: Total value
        """
        return sum(book.price * book.quantity for book in self.books.values())
    
    def __len__(self):
        """
        Get the number of books in inventory.
        
        Returns:
            int: Number of books
        """
        return len(self.books)
    
    def __str__(self):
        """
        String representation of the inventory.
        
        Returns:
            str: Formatted string with inventory information
        """
        return f"Inventory with {len(self)} books, total value: ${self.total_inventory_value():.2f}"
