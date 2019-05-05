class Account():
    
    def __init__(self, owner, balance):
        
        self.owner = owner
        self.balance = balance
    
    def deposit(self, num):
        
        print("{} was just added to your acount".format(num))
        self.balance = self.balance + num
    
    def __str__(self):
        return  "Account owner = {} \nYour Balance = {}".format(self.owner, self.balance)
        
    
    def withdraw(self, num):
        
        if num <= self.balance:
            self.balance = self.balance - num
            print("Your new balance = {}".format(self.balance))
        else:
            print("Not enough funds")
        
        return self.balance
        
acc1 = Account('Casey', 1000)


acc1.withdraw(500)
acc1.withdraw(500)
acc1.withdraw(1)
print(acc1)


