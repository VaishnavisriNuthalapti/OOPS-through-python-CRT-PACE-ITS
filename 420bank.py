#class body
class ippb:
    def __init__(self):
        self.balance=0
        print("Welcome to ippb")
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance+=amount
        print("\n Amount deposited: ",amount)
    def withdraw(self):
        amount=float(input("Amount to be withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("Amount withdrawn: ",amount)
        else:
            print("\n insufficient balance")
    def display(self):
        print("Net available balance=",self.balance)


#driver code
s=ippb()
s.deposit()
s.withdraw()
s.display()






    
