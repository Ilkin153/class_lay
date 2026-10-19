class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposited amount must be positive...")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdraw {amount}. New balance is {self.balance}.")
            else:
                print("Insufficent funds...")
    def show_balance(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}...")