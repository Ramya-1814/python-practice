class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
            self.balance += amount
            print(amount, "is deposited successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "is withdrawn successfully.")
        else:
            print("Insufficient Balance.")

    def display(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)



name = input("Enter the name of the account holder:")
balance = float(input("Enter the initial balance:"))
account1 = BankAccount(name,balance)
account1.display()

deposit_amount = float(input("Enter the amount to deposit:"))
account1.deposit(deposit_amount)
account1.display()

withdraw_amount = float(input("Enter the amount to withdraw:"))
account1.withdraw(withdraw_amount)
account1.display()