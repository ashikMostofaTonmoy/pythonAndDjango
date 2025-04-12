"""
Cart Controller for Online Bookstore Management System

This module defines the CartController class which handles shopping cart operations.
"""

class CartController:
    """
    Handles shopping cart operations.
    
    Attributes:
        auth_controller (AuthController): Authentication controller for user access
        book_controller (BookController): Book controller for book access
    """
    
    def __init__(self, auth_controller, book_controller):
        """
        Initialize a new CartController instance.
        
        Args:
            auth_controller (AuthController): Authentication controller for user access
            book_controller (BookController): Book controller for book access
        """
        self.auth_controller = auth_controller
        self.book_controller = book_controller
    
    def add_to_cart(self, book_id, quantity=1):
        """
        Add a book to the current user's cart.
        
        Args:
            book_id (str): ID of book to add
            quantity (int, optional): Quantity to add. Defaults to 1.
            
        Returns:
            bool: True if added successfully, False if not logged in, book not found, or not enough in stock
        """
        user = self.auth_controller.get_current_user()
        if not user:
            return False
        
        book = self.book_controller.get_book(book_id)
        if not book:
            return False
        
        return user.add_to_cart(book, quantity)
    
    def remove_from_cart(self, book_id):
        """
        Remove a book from the current user's cart.
        
        Args:
            book_id (str): ID of book to remove
            
        Returns:
            bool: True if removed, False if not logged in or not found
        """
        user = self.auth_controller.get_current_user()
        if not user:
            return False
        
        return user.remove_from_cart(book_id)
    
    def update_cart_quantity(self, book_id, quantity):
        """
        Update quantity of a book in the current user's cart.
        
        Args:
            book_id (str): ID of book to update
            quantity (int): New quantity
            
        Returns:
            bool: True if updated, False if not logged in, not found, or invalid quantity
        """
        user = self.auth_controller.get_current_user()
        if not user:
            return False
        
        return user.update_cart_quantity(book_id, quantity)
    
    def get_cart(self):
        """
        Get the current user's cart.
        
        Returns:
            list: List of cart items, empty list if not logged in
        """
        user = self.auth_controller.get_current_user()
        if not user:
            return []
        
        return user.cart
    
    def get_cart_total(self):
        """
        Calculate the total price of items in the current user's cart.
        
        Returns:
            float: Total price, 0 if not logged in
        """
        user = self.auth_controller.get_current_user()
        if not user:
            return 0
        
        return user.get_cart_total()
    
    def clear_cart(self):
        """
        Clear all items from the current user's cart.
        
        Returns:
            bool: True if cleared, False if not logged in
        """
        user = self.auth_controller.get_current_user()
        if not user:
            return False
        
        user.clear_cart()
        return True
    
    def checkout(self, order_id, payment_method):
        """
        Checkout the current user's cart and place an order.
        
        Args:
            order_id (str): Unique identifier for the order
            payment_method (str): Method of payment
            
        Returns:
            dict: Order information if successful, None if not logged in or cart empty
        """
        user = self.auth_controller.get_current_user()
        if not user:
            return None
        
        return user.place_order(order_id, payment_method)
    
    def get_order_history(self):
        """
        Get the current user's order history.
        
        Returns:
            list: List of past orders, empty list if not logged in
        """
        user = self.auth_controller.get_current_user()
        if not user:
            return []
        
        return user.get_order_history()
