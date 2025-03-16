# 3. Create a class for accounting
# Create a class called BankAccount that has properties like balance and owner.
# Create methods to deposit () and withdraw () from the account.
# Also create a method called display_balance () that displays the account balance.

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance >= amount:
             self.balance -= amount
        else:
            print("mojoodi kafi nist!")
    
    def balance_display(self):
        print(f"owner = {self.owner},balance = {self.balance}")
        

account = BankAccount("Ali",10000)
account.deposit(500)
account.withdraw(700)
account.balance_display()     