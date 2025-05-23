class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance

class SavingsAccount:
    def __init__(self, account_number, balance, interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
