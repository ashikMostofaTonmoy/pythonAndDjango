"""
User Model for Online Bookstore Management System

This module defines the User class which represents a user in the bookstore system.
"""

class User:
    """
    Represents a user in the bookstore system.
    
    Attributes:
        user_id (str): Unique identifier for the user
        username (str): Username for login
        password (str): Hashed password (in a real system, this would be properly hashed)
        name (str): Full name of the user
        email (str): Email address of the user
        address (str): Shipping address of the user
        is_admin (bool): Whether the user has admin privileges
    """
    
    def __init__(self, user_id, username, password, name, email, address, is_admin=False):
        """
        Initialize a new User instance.
        
        Args:
            user_id (str): Unique identifier for the user
            username (str): Username for login
            password (str): Password (would be hashed in a real system)
            name (str): Full name of the user
            email (str): Email address of the user
            address (str): Shipping address of the user
            is_admin (bool, optional): Whether the user has admin privileges. Defaults to False.
        """
        self.user_id = user_id
        self.username = username
        self.password = password  # In a real system, this would be hashed
        self.name = name
        self.email = email
        self.address = address
        self.is_admin = is_admin
        self.cart = []  # List to store cart items
        self.order_history = []  # List to store past orders
    
    def authenticate(self, password):
        """
        Authenticate the user with a password.
        
        Args:
            password (str): Password to check
            
        Returns:
            bool: True if password matches, False otherwise
        """
        # In a real system, this would compare hashed passwords
        return self.password == password
    
    def update_profile(self, name=None, email=None, address=None):
        """
        Update user profile information.
        
        Args:
            name (str, optional): New name. Defaults to None.
            email (str, optional): New email. Defaults to None.
            address (str, optional): New address. Defaults to None.
            
        Returns:
            dict: Updated user information
        """
        if name:
            self.name = name
        if email:
            self.email = email
        if address:
            self.address = address
        
        return self.get_info()
    
    def add_to_cart(self, book, quantity=1):
        """
        Add a book to the user's cart.
        
        Args:
            book (Book): Book to add to cart
            quantity (int, optional): Quantity to add. Defaults to 1.
            
        Returns:
            bool: True if added successfully, False if not enough in stock
        """
        if book.quantity < quantity:
            return False
        
        # Check if book already in cart
        for item in self.cart:
            if item['book'].book_id == book.book_id:
                item['quantity'] += quantity
                return True
        
        # Add new item to cart
        self.cart.append({'book': book, 'quantity': quantity})
        return True
    
    def remove_from_cart(self, book_id):
        """
        Remove a book from the user's cart.
        
        Args:
            book_id (str): ID of book to remove
            
        Returns:
            bool: True if removed, False if not found
        """
        for i, item in enumerate(self.cart):
            if item['book'].book_id == book_id:
                self.cart.pop(i)
                return True
        return False
    
    def update_cart_quantity(self, book_id, quantity):
        """
        Update quantity of a book in the cart.
        
        Args:
            book_id (str): ID of book to update
            quantity (int): New quantity
            
        Returns:
            bool: True if updated, False if not found or invalid quantity
        """
        if quantity <= 0:
            return self.remove_from_cart(book_id)
        
        for item in self.cart:
            if item['book'].book_id == book_id:
                if item['book'].quantity < quantity:
                    return False
                item['quantity'] = quantity
                return True
        return False
    
    def get_cart_total(self):
        """
        Calculate the total price of items in the cart.
        
        Returns:
            float: Total price
        """
        return sum(item['book'].price * item['quantity'] for item in self.cart)
    
    def clear_cart(self):
        """
        Clear all items from the cart.
        """
        self.cart = []
    
    def place_order(self, order_id, payment_method):
        """
        Place an order with the current cart items.
        
        Args:
            order_id (str): Unique identifier for the order
            payment_method (str): Method of payment
            
        Returns:
            dict: Order information
        """
        if not self.cart:
            return None
        
        # Create order from cart
        order = {
            'order_id': order_id,
            'user_id': self.user_id,
            'items': [],
            'total': self.get_cart_total(),
            'payment_method': payment_method,
            'status': 'Placed'
        }
        
        # Add items and update inventory
        for item in self.cart:
            book = item['book']
            quantity = item['quantity']
            
            # Update book quantity
            if not book.update_quantity(-quantity):
                # Rollback previous updates if any item fails
                for prev_item in order['items']:
                    prev_item['book'].update_quantity(prev_item['quantity'])
                return None
            
            order['items'].append({
                'book': book,
                'quantity': quantity,
                'price': book.price
            })
        
        # Add to order history and clear cart
        self.order_history.append(order)
        self.clear_cart()
        
        return order
    
    def get_order_history(self):
        """
        Get the user's order history.
        
        Returns:
            list: List of past orders
        """
        return self.order_history
    
    def get_info(self):
        """
        Get a dictionary with user information.
        
        Returns:
            dict: Dictionary containing user information (excluding password)
        """
        return {
            'user_id': self.user_id,
            'username': self.username,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'is_admin': self.is_admin
        }
    
    def __str__(self):
        """
        String representation of the user.
        
        Returns:
            str: Formatted string with user information
        """
        return f"{self.name} ({self.username}) - {'Admin' if self.is_admin else 'Customer'}"
