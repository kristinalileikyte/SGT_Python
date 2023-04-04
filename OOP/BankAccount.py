class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance
    
    def withdraw(self, withdraw):
        self.balance -= withdraw
        return self.balance
    

bankAccount = BankAccount(11234567, 171.52, "Kristina")

print(bankAccount.deposit(22.85))
print(bankAccount.withdraw(19.23))