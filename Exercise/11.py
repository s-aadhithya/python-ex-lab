class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful. Current balance:", self.balance)
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

    def __add__(self, other):
        new_balance = self.balance + other.balance
        return BankAccount("Combined Account", "Joint Account", new_balance)

    def __sub__(self, other):
        new_balance = self.balance - other.balance
        return BankAccount("Difference Account", "Difference Holder", new_balance)

    def __eq__(self, other):
        return self.account_number == other.account_number

account1 = BankAccount("A001", "John Doe", 1000)
account2 = BankAccount("A002", "Jane Smith", 500)
account3 = BankAccount("A001", "Adam Johnson", 1500)
print(account1 == account2)
print(account1 == account3)
combined_account = account1 + account2
combined_account.display_account_info()
difference_account = account1 - account2
difference_account.display_account_info()
