# defined a bank acount here (the balnce sholud've started at 0.0)
# set the account to accept money and withdraw that money

class BankAccount:
    
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0

    def deposit(self,money):
        self.balance += money
        return self.balance
    
    def withdraw(self,money):
        self.balance -= money
        return self.balance
    
actt = BankAccount("Jerry")
print(actt.owner)
print(actt.balance)
print(actt.deposit(100))
print(actt.withdraw(45))
print(actt.balance)
    