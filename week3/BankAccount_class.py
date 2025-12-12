class BankAccount:
    def __init__(self):
        self.__balance = 0   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds! Withdrawal denied.")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def get_balance(self):
        return self.__balance



acc = BankAccount()
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(400)   
print("Final Balance:", acc.get_balance())
