# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        This is the constructor method.
        It runs automatically when you create a BankAccount object.
        initial_balance defaults to 0 if not provided.
        """
        self.account_balance = initial_balance  # set the starting balance

    def deposit(self, amount):
        """Add money to the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw money if enough funds exist.
        Returns True if successful, False if insufficient balance.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")
