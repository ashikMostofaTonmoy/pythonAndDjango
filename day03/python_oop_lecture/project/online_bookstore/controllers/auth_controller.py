"""
Authentication Controller for Online Bookstore Management System

This module defines the AuthController class which handles user authentication.
"""

class AuthController:
    """
    Handles user authentication and user management.
    
    Attributes:
        users (dict): Dictionary of users with username as key and User object as value
    """
    
    def __init__(self):
        """
        Initialize a new AuthController instance.
        """
        self.users = {}
        self.current_user = None
    
    def register_user(self, user):
        """
        Register a new user.
        
        Args:
            user: User object to register
            
        Returns:
            bool: True if registered successfully, False if username already exists
        """
        if user.username in self.users:
            return False
        
        self.users[user.username] = user
        return True
    
    def login(self, username, password):
        """
        Authenticate and login a user.
        
        Args:
            username (str): Username to login
            password (str): Password to authenticate
            
        Returns:
            User: User object if login successful, None otherwise
        """
        user = self.users.get(username)
        if user and user.authenticate(password):
            self.current_user = user
            return user
        return None
    
    def logout(self):
        """
        Logout the current user.
        
        Returns:
            bool: True if logout successful, False if no user logged in
        """
        if self.current_user:
            self.current_user = None
            return True
        return False
    
    def get_current_user(self):
        """
        Get the currently logged in user.
        
        Returns:
            User: Current user object, None if no user logged in
        """
        return self.current_user
    
    def is_logged_in(self):
        """
        Check if a user is currently logged in.
        
        Returns:
            bool: True if a user is logged in, False otherwise
        """
        return self.current_user is not None
    
    def is_admin(self):
        """
        Check if the current user is an admin.
        
        Returns:
            bool: True if current user is an admin, False otherwise
        """
        return self.current_user is not None and self.current_user.is_admin
    
    def get_user(self, username):
        """
        Get a user by username.
        
        Args:
            username (str): Username to get
            
        Returns:
            User: User object if found, None otherwise
        """
        return self.users.get(username)
    
    def get_all_users(self):
        """
        Get all registered users.
        
        Returns:
            list: List of all User objects
        """
        return list(self.users.values())
    
    def update_user(self, username, **kwargs):
        """
        Update user information.
        
        Args:
            username (str): Username of user to update
            **kwargs: Attributes to update
            
        Returns:
            bool: True if updated, False if not found
        """
        user = self.get_user(username)
        if not user:
            return False
        
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        
        return True
    
    def delete_user(self, username):
        """
        Delete a user.
        
        Args:
            username (str): Username of user to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        if username in self.users:
            # Logout if deleting current user
            if self.current_user and self.current_user.username == username:
                self.logout()
            
            del self.users[username]
            return True
        return False
