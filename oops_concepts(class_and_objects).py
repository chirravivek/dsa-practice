class BankAccount :
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"{self.name} deposited {amount}. New balance is {self.balance}")
    def withdraw(self,amount) :
        if amount > self.balance :
            print(f"not enougth balance")
        else :
            self.balance = self.balance - amount
    
    def show_balance(self):
        print(f"{self.name}'s balance is {self.balance}")
        
account = BankAccount("Vivek", 1000) 
account.show_balance()   
account.deposit(500)   
account.withdraw(200)    
account.withdraw(2000)   
account.show_balance()
        
     
        