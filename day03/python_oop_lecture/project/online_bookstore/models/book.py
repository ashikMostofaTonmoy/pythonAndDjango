"""
Book Model for Online Bookstore Management System

This module defines the Book class which represents a book in the bookstore inventory.
"""

class Book:
    """
    Represents a book in the bookstore inventory.
    
    Attributes:
        book_id (str): Unique identifier for the book
        title (str): Title of the book
        author (str): Author of the book
        isbn (str): ISBN number of the book
        price (float): Price of the book
        quantity (int): Available quantity in stock
        genre (str): Genre of the book
        publisher (str): Publisher of the book
        publication_year (int): Year the book was published
    """
    
    def __init__(self, book_id, title, author, isbn, price, quantity, genre, publisher, publication_year):
        """
        Initialize a new Book instance.
        
        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
            isbn (str): ISBN number of the book
            price (float): Price of the book
            quantity (int): Available quantity in stock
            genre (str): Genre of the book
            publisher (str): Publisher of the book
            publication_year (int): Year the book was published
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.quantity = quantity
        self.genre = genre
        self.publisher = publisher
        self.publication_year = publication_year
    
    def update_quantity(self, amount):
        """
        Update the quantity of books in stock.
        
        Args:
            amount (int): Amount to add to the quantity (negative to reduce)
            
        Returns:
            bool: True if update successful, False if would result in negative quantity
        """
        if self.quantity + amount < 0:
            return False
        self.quantity += amount
        return True
    
    def update_price(self, new_price):
        """
        Update the price of the book.
        
        Args:
            new_price (float): New price for the book
            
        Returns:
            bool: True if update successful, False if invalid price
        """
        if new_price < 0:
            return False
        self.price = new_price
        return True
    
    def is_available(self):
        """
        Check if the book is available in stock.
        
        Returns:
            bool: True if quantity > 0, False otherwise
        """
        return self.quantity > 0
    
    def get_info(self):
        """
        Get a dictionary with book information.
        
        Returns:
            dict: Dictionary containing book information
        """
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'price': self.price,
            'quantity': self.quantity,
            'genre': self.genre,
            'publisher': self.publisher,
            'publication_year': self.publication_year
        }
    
    def __str__(self):
        """
        String representation of the book.
        
        Returns:
            str: Formatted string with book information
        """
        return f"{self.title} by {self.author} (${self.price}) - {self.quantity} in stock"
    
    def __repr__(self):
        """
        Official string representation of the book.
        
        Returns:
            str: String representation for debugging
        """
        return f"Book('{self.book_id}', '{self.title}', '{self.author}', '{self.isbn}', {self.price}, {self.quantity}, '{self.genre}', '{self.publisher}', {self.publication_year})"
