#!/usr/bin/env python3
# Personal Budget Tracker
# A tool to track personal finances with file operations

import os
import csv
import datetime
from collections import defaultdict


class BudgetTracker:
    def __init__(self, file_path="transactions.csv"):
        self.file_path = file_path
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        """Load transactions from the CSV file."""
        if not os.path.exists(self.file_path):
            # Create file with headers if it doesn't exist
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    ['Date', 'Type', 'Category', 'Amount', 'Description'])
            return

        with open(self.file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            self.transactions = list(reader)

            # Convert amount from string to float
            for transaction in self.transactions:
                transaction['Amount'] = float(transaction['Amount'])

    def save_transactions(self):
        """Save transactions to the CSV file."""
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ['Date', 'Type', 'Category', 'Amount', 'Description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.transactions)

    def add_transaction(self, transaction_type, category, amount, description, date=None):
        """Add a new transaction."""
        if date is None:
            date = datetime.datetime.now().strftime('%Y-%m-%d')

        # Validate amount
        try:
            amount = float(amount)
        except ValueError:
            print("Error: Amount must be a number.")
            return False

        transaction = {
            'Date': date,
            'Type': transaction_type,
            'Category': category,
            'Amount': amount,
            'Description': description
        }

        self.transactions.append(transaction)
        self.save_transactions()
        print(f"{transaction_type} of ${amount:.2f} added successfully.")
        return True

    def get_all_transactions(self):
        """Return all transactions."""
        return self.transactions

    def search_transactions(self, keyword):
        """Search transactions by keyword in any field."""
        results = []
        keyword = keyword.lower()

        for transaction in self.transactions:
            for key, value in transaction.items():
                if keyword in str(value).lower():
                    results.append(transaction)
                    break

        return results

    def filter_by_date_range(self, start_date, end_date):
        """Filter transactions by date range."""
        results = []

        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return []

        for transaction in self.transactions:
            trans_date = datetime.datetime.strptime(
                transaction['Date'], '%Y-%m-%d').date()
            if start <= trans_date <= end:
                results.append(transaction)

        return results

    def filter_by_category(self, category):
        """Filter transactions by category."""
        return [t for t in self.transactions if t['Category'].lower() == category.lower()]

    def filter_by_type(self, transaction_type):
        """Filter transactions by type (income/expense)."""
        return [t for t in self.transactions if t['Type'].lower() == transaction_type.lower()]

    def get_monthly_report(self, year=None, month=None):
        """Generate a monthly report."""
        if year is None or month is None:
            now = datetime.datetime.now()
            year = now.year
            month = now.month

        # Format month to two digits
        month_str = f"{month:02d}"

        # Filter transactions for the specified month
        monthly_transactions = []
        for transaction in self.transactions:
            date_parts = transaction['Date'].split('-')
            if date_parts[0] == str(year) and date_parts[1] == month_str:
                monthly_transactions.append(transaction)

        # Calculate totals
        income = sum(t['Amount']
                     for t in monthly_transactions if t['Type'].lower() == 'income')
        expenses = sum(t['Amount']
                       for t in monthly_transactions if t['Type'].lower() == 'expense')
        balance = income - expenses

        # Group expenses by category
        categories = defaultdict(float)
        for transaction in monthly_transactions:
            if transaction['Type'].lower() == 'expense':
                categories[transaction['Category']] += transaction['Amount']

        return {
            'total_income': income,
            'total_expenses': expenses,
            'balance': balance,
            'expenses_by_category': dict(categories),
            'transactions': monthly_transactions
        }

    def get_balance(self):
        """Calculate the current balance."""
        income = sum(t['Amount']
                     for t in self.transactions if t['Type'].lower() == 'income')
        expenses = sum(t['Amount']
                       for t in self.transactions if t['Type'].lower() == 'expense')
        return income - expenses


def display_menu():
    """Display the main menu."""
    print("\n===== Personal Budget Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. Search Transactions")
    print("5. View Monthly Report")
    print("6. View Current Balance")
    print("7. Exit")
    return input("Enter your choice (1-7): ")


def get_transaction_details():
    """Get transaction details from user."""
    category = input("Enter category: ")

    while True:
        try:
            amount = float(input("Enter amount: $"))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    description = input("Enter description: ")

    date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    date = date_input if date_input else None

    return category, amount, description, date


def display_transactions(transactions):
    """Display transactions in a formatted way."""
    if not transactions:
        print("No transactions found.")
        return

    print("\n{:<12} {:<10} {:<15} {:<10} {:<20}".format(
        "Date", "Type", "Category", "Amount", "Description"))
    print("-" * 70)

    for t in transactions:
        print("{:<12} {:<10} {:<15} ${:<9.2f} {:<20}".format(
            t['Date'], t['Type'], t['Category'], t['Amount'], t['Description']))


def display_monthly_report(report):
    """Display monthly report."""
    print("\n===== Monthly Report =====")
    print(f"Total Income: ${report['total_income']:.2f}")
    print(f"Total Expenses: ${report['total_expenses']:.2f}")
    print(f"Balance: ${report['balance']:.2f}")

    print("\nExpenses by Category:")
    for category, amount in report['expenses_by_category'].items():
        print(f"  {category}: ${amount:.2f}")

    print("\nTransactions:")
    display_transactions(report['transactions'])


def main():
    tracker = BudgetTracker()

    while True:
        choice = display_menu()

        if choice == '1':  # Add Income
            category, amount, description, date = get_transaction_details()
            tracker.add_transaction(
                'Income', category, amount, description, date)

        elif choice == '2':  # Add Expense
            category, amount, description, date = get_transaction_details()
            tracker.add_transaction(
                'Expense', category, amount, description, date)

        elif choice == '3':  # View All Transactions
            print("\n===== All Transactions =====")
            display_transactions(tracker.get_all_transactions())

        elif choice == '4':  # Search Transactions
            keyword = input("Enter search term: ")
            results = tracker.search_transactions(keyword)
            print(f"\n===== Search Results for '{keyword}' =====")
            display_transactions(results)

        elif choice == '5':  # View Monthly Report
            year_input = input(
                "Enter year (YYYY) or leave blank for current year: ")
            month_input = input(
                "Enter month (1-12) or leave blank for current month: ")

            year = int(year_input) if year_input else None
            month = int(month_input) if month_input else None

            report = tracker.get_monthly_report(year, month)
            display_monthly_report(report)

        elif choice == '6':  # View Current Balance
            balance = tracker.get_balance()
            print(f"\nCurrent Balance: ${balance:.2f}")

        elif choice == '7':  # Exit
            print("Thank you for using the Personal Budget Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
