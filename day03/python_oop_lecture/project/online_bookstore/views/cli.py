"""
Command Line Interface View for Online Bookstore Management System

This module defines the CLI class which provides a text-based interface for the bookstore system.
"""

class CLI:
    """
    Provides a text-based interface for the bookstore system.
    
    Attributes:
        auth_controller (AuthController): Authentication controller
        book_controller (BookController): Book controller
        cart_controller (CartController): Cart controller
    """
    
    def __init__(self, auth_controller, book_controller, cart_controller):
        """
        Initialize a new CLI instance.
        
        Args:
            auth_controller (AuthController): Authentication controller
            book_controller (BookController): Book controller
            cart_controller (CartController): Cart controller
        """
        self.auth_controller = auth_controller
        self.book_controller = book_controller
        self.cart_controller = cart_controller
    
    def display_welcome(self):
        """
        Display welcome message.
        """
        print("=" * 50)
        print("Welcome to the Online Bookstore Management System")
        print("=" * 50)
    
    def display_menu(self):
        """
        Display main menu.
        """
        print("\nMain Menu:")
        print("1. Login")
        print("2. Register")
        print("3. Browse Books")
        print("4. Search Books")
        print("5. Exit")
        
        if self.auth_controller.is_logged_in():
            user = self.auth_controller.get_current_user()
            print("\nUser Menu:")
            print("6. View Cart")
            print("7. Checkout")
            print("8. View Order History")
            print("9. Logout")
            
            if self.auth_controller.is_admin():
                print("\nAdmin Menu:")
                print("10. Add Book")
                print("11. Update Book")
                print("12. Remove Book")
                print("13. View Low Stock Books")
                print("14. View Inventory Value")
    
    def login(self):
        """
        Handle user login.
        """
        print("\n--- Login ---")
        username = input("Username: ")
        password = input("Password: ")
        
        user = self.auth_controller.login(username, password)
        if user:
            print(f"Welcome back, {user.name}!")
        else:
            print("Invalid username or password.")
    
    def register(self):
        """
        Handle user registration.
        """
        print("\n--- Register ---")
        user_id = input("User ID: ")
        username = input("Username: ")
        password = input("Password: ")
        name = input("Full Name: ")
        email = input("Email: ")
        address = input("Address: ")
        
        from ..models.user import User
        user = User(user_id, username, password, name, email, address)
        
        if self.auth_controller.register_user(user):
            print(f"Registration successful! Welcome, {name}!")
        else:
            print("Username already exists.")
    
    def browse_books(self):
        """
        Display all books.
        """
        print("\n--- Book Catalog ---")
        books = self.book_controller.get_all_books()
        
        if not books:
            print("No books available.")
            return
        
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")
        
        if self.auth_controller.is_logged_in():
            self.prompt_add_to_cart(books)
    
    def search_books(self):
        """
        Search for books.
        """
        print("\n--- Search Books ---")
        print("1. Search by Title")
        print("2. Search by Author")
        print("3. Search by Genre")
        choice = input("Enter choice (1-3): ")
        
        if choice == "1":
            title = input("Enter title: ")
            books = self.book_controller.search_books(title=title)
        elif choice == "2":
            author = input("Enter author: ")
            books = self.book_controller.get_books_by_author(author)
        elif choice == "3":
            genre = input("Enter genre: ")
            books = self.book_controller.get_books_by_genre(genre)
        else:
            print("Invalid choice.")
            return
        
        if not books:
            print("No books found.")
            return
        
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")
        
        if self.auth_controller.is_logged_in():
            self.prompt_add_to_cart(books)
    
    def prompt_add_to_cart(self, books):
        """
        Prompt user to add a book to cart.
        
        Args:
            books (list): List of Book objects
        """
        choice = input("\nAdd a book to cart? (y/n): ")
        if choice.lower() != 'y':
            return
        
        book_num = input("Enter book number: ")
        try:
            book_num = int(book_num)
            if book_num < 1 or book_num > len(books):
                print("Invalid book number.")
                return
            
            book = books[book_num - 1]
            quantity = input("Enter quantity: ")
            try:
                quantity = int(quantity)
                if quantity < 1:
                    print("Quantity must be positive.")
                    return
                
                if self.cart_controller.add_to_cart(book.book_id, quantity):
                    print(f"Added {quantity} copy/copies of '{book.title}' to cart.")
                else:
                    print("Failed to add to cart. Not enough in stock.")
            except ValueError:
                print("Invalid quantity.")
        except ValueError:
            print("Invalid book number.")
    
    def view_cart(self):
        """
        Display current user's cart.
        """
        if not self.auth_controller.is_logged_in():
            print("You must be logged in to view cart.")
            return
        
        print("\n--- Your Cart ---")
        cart = self.cart_controller.get_cart()
        
        if not cart:
            print("Your cart is empty.")
            return
        
        for i, item in enumerate(cart, 1):
            book = item['book']
            quantity = item['quantity']
            total = book.price * quantity
            print(f"{i}. {book.title} - ${book.price} x {quantity} = ${total}")
        
        print(f"\nTotal: ${self.cart_controller.get_cart_total()}")
        
        print("\nCart Options:")
        print("1. Update Quantity")
        print("2. Remove Item")
        print("3. Clear Cart")
        print("4. Back to Main Menu")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            self.update_cart_quantity()
        elif choice == "2":
            self.remove_from_cart()
        elif choice == "3":
            self.clear_cart()
    
    def update_cart_quantity(self):
        """
        Update quantity of an item in cart.
        """
        cart = self.cart_controller.get_cart()
        item_num = input("Enter item number: ")
        
        try:
            item_num = int(item_num)
            if item_num < 1 or item_num > len(cart):
                print("Invalid item number.")
                return
            
            item = cart[item_num - 1]
            book_id = item['book'].book_id
            
            quantity = input("Enter new quantity: ")
            try:
                quantity = int(quantity)
                if quantity < 0:
                    print("Quantity must be non-negative.")
                    return
                
                if self.cart_controller.update_cart_quantity(book_id, quantity):
                    print("Quantity updated.")
                else:
                    print("Failed to update quantity. Not enough in stock.")
            except ValueError:
                print("Invalid quantity.")
        except ValueError:
            print("Invalid item number.")
    
    def remove_from_cart(self):
        """
        Remove an item from cart.
        """
        cart = self.cart_controller.get_cart()
        item_num = input("Enter item number: ")
        
        try:
            item_num = int(item_num)
            if item_num < 1 or item_num > len(cart):
                print("Invalid item number.")
                return
            
            item = cart[item_num - 1]
            book_id = item['book'].book_id
            
            if self.cart_controller.remove_from_cart(book_id):
                print("Item removed from cart.")
            else:
                print("Failed to remove item.")
        except ValueError:
            print("Invalid item number.")
    
    def clear_cart(self):
        """
        Clear all items from cart.
        """
        confirm = input("Are you sure you want to clear your cart? (y/n): ")
        if confirm.lower() == 'y':
            if self.cart_controller.clear_cart():
                print("Cart cleared.")
            else:
                print("Failed to clear cart.")
    
    def checkout(self):
        """
        Checkout and place an order.
        """
        if not self.auth_controller.is_logged_in():
            print("You must be logged in to checkout.")
            return
        
        cart = self.cart_controller.get_cart()
        if not cart:
            print("Your cart is empty.")
            return
        
        print("\n--- Checkout ---")
        print("Cart Summary:")
        
        for i, item in enumerate(cart, 1):
            book = item['book']
            quantity = item['quantity']
            total = book.price * quantity
            print(f"{i}. {book.title} - ${book.price} x {quantity} = ${total}")
        
        print(f"\nTotal: ${self.cart_controller.get_cart_total()}")
        
        confirm = input("Proceed with checkout? (y/n): ")
        if confirm.lower() != 'y':
            return
        
        payment_method = input("Enter payment method: ")
        import uuid
        order_id = str(uuid.uuid4())
        
        order = self.cart_controller.checkout(order_id, payment_method)
        if order:
            print(f"Order placed successfully! Order ID: {order_id}")
        else:
            print("Failed to place order. Please check stock availability.")
    
    def view_order_history(self):
        """
        Display current user's order history.
        """
        if not self.auth_controller.is_logged_in():
            print("You must be logged in to view order history.")
            return
        
        print("\n--- Order History ---")
        orders = self.cart_controller.get_order_history()
        
        if not orders:
            print("No orders found.")
            return
        
        for order in orders:
            print(f"Order ID: {order['order_id']}")
            print(f"Status: {order['status']}")
            print(f"Payment Method: {order['payment_method']}")
            print("Items:")
            
            for item in order['items']:
                book = item['book']
                quantity = item['quantity']
                price = item['price']
                total = price * quantity
                print(f"- {book.title} - ${price} x {quantity} = ${total}")
            
            print(f"Total: ${order['total']}")
            print("-" * 30)
    
    def add_book(self):
        """
        Add a new book to inventory (admin only).
        """
        if not self.auth_controller.is_admin():
            print("Admin access required.")
            return
        
        print("\n--- Add Book ---")
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        
        try:
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            publication_year = int(input("Publication Year: "))
        except ValueError:
            print("Invalid numeric input.")
            return
        
        genre = input("Genre: ")
        publisher = input("Publisher: ")
        
        from ..models.book import Book
        book = Book(book_id, title, author, isbn, price, quantity, genre, publisher, publication_year)
        
        if self.book_controller.add_book(book):
            print(f"Book '{title}' added successfully.")
        else:
            print("Failed to add book. Book ID may already exist.")
    
    def update_book(self):
        """
        Update book information (admin only).
        """
        if not self.auth_controller.is_admin():
            print("Admin access required.")
            return
        
        print("\n--- Update Book ---")
        book_id = input("Enter Book ID to update: ")
        
        book = self.book_controller.get_book(book_id)
        if not book:
            print("Book not found.")
            return
        
        print(f"Updating book: {book}")
        
        updates = {}
        title = input("New Title (leave empty to keep current): ")
        if title:
            updates['title'] = title
        
        author = input("New Author (leave empty to keep current): ")
        if author:
            updates['author'] = author
        
        price_str = input("New Price (leave empty to keep current): ")
        if price_str:
            try:
                updates['price'] = float(price_str)
            except ValueError:
                print("Invalid price. Skipping price update.")
        
        quantity_str = input("New Quantity (leave empty to keep current): ")
        if quantity_str:
            try:
                updates['quantity'] = int(quantity_str)
            except ValueError:
                print("Invalid quantity. Skipping quantity update.")
        
        genre = input("New Genre (leave empty to keep current): ")
        if genre:
            updates['genre'] = genre
        
        if self.book_controller.update_book(book_id, **updates):
            print("Book updated successfully.")
        else:
            print("Failed to update book.")
    
    def remove_book(self):
        """
        Remove a book from inventory (admin only).
        """
        if not self.auth_controller.is_admin():
            print("Admin access required.")
            return
        
        print("\n--- Remove Book ---")
        book_id = input("Enter Book ID to remove: ")
        
        book = self.book_controller.get_book(book_id)
        if not book:
            print("Book not found.")
            return
        
        confirm = input(f"Are you sure you want to remove '{book.title}'? (y/n): ")
        if confirm.lower() == 'y':
            if self.book_controller.remove_book(book_id):
                print("Book removed successfully.")
            else:
                print("Failed to remove book.")
    
    def view_low_stock(self):
        """
        Display books with low stock (admin only).
        """
        if not self.auth_controller.is_admin():
            print("Admin access required.")
            return
        
        print("\n--- Low Stock Books ---")
        threshold_str = input("Enter stock threshold (default 5): ")
        
        try:
            threshold = int(threshold_str) if threshold_str else 5
            books = self.book_controller.get_low_stock_books(threshold)
            
            if not books:
                print(f"No books with stock below {threshold}.")
                return
            
            for i, book in enumerate(books, 1):
                print(f"{i}. {book.title} - {book.quantity} in stock")
        except ValueError:
            print("Invalid threshold.")
    
    def view_inventory_value(self):
        """
        Display total inventory value (admin only).
        """
        if not self.auth_controller.is_admin():
            print("Admin access required.")
            return
        
        value = self.book_controller.total_inventory_value()
        print(f"\nTotal Inventory Value: ${value:.2f}")
    
    def logout(self):
        """
        Logout current user.
        """
        if self.auth_controller.logout():
            print("Logged out successfully.")
        else:
            print("No user logged in.")
    
    def run(self):
        """
        Run the CLI application.
        """
        self.display_welcome()
        
        while True:
            self.display_menu()
            choice = input("\nEnter choice: ")
            
            if choice == "1":
                self.login()
            elif choice == "2":
                self.register()
            elif choice == "3":
                self.browse_books()
            elif choice == "4":
                self.search_books()
            elif choice == "5":
                print("Thank you for using the Online Bookstore Management System!")
                break
            elif choice == "6" and self.auth_controller.is_logged_in():
                self.view_cart()
            elif choice == "7" and self.auth_controller.is_logged_in():
                self.checkout()
            elif choice == "8" and self.auth_controller.is_logged_in():
                self.view_order_history()
            elif choice == "9" and self.auth_controller.is_logged_in():
                self.logout()
            elif choice == "10" and self.auth_controller.is_admin():
                self.add_book()
            elif choice == "11" and self.auth_controller.is_admin():
                self.update_book()
            elif choice == "12" and self.auth_controller.is_admin():
                self.remove_book()
            elif choice == "13" and self.auth_controller.is_admin():
                self.view_low_stock()
            elif choice == "14" and self.auth_controller.is_admin():
                self.view_inventory_value()
            else:
                print("Invalid choice or insufficient permissions.")
