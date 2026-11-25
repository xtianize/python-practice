#Wallet class - OOP

class Wallet:
        def __init__(self,owner,balance=500.00):
            self.owner=owner
            self.balance=balance
            
        def __validate(self,amt):
            if amt<0:
                print(self.owner+" account: Transaction failed. Invalid amount.")
                return False
            else:
                return True
              
        def cash_in(self,amt):
             if self.__validate(amt):
                 self.balance+=amt
                 print(self.owner+" account: Transaction successful. Amount added:",amt)
             return self.balance
                
        def send_money(self,amt,target_owner):
             if self.__validate(amt):
                 if amt>self.balance:
                        print(self.owner+" account: Transaction failed. Account does not have enough balance.")
                        return self.balance
                 else:
                        self.balance-=amt
                        target_owner.cash_in(amt)
                        print(self.owner+" Transaction successful. Amount sent to",target_owner.owner+":",amt)
             return self.balance
                
        def check_balance(self):
             return self.balance
              
#creating 2 wallet accounts
w1=Wallet('Alex',1000)
w2=Wallet('Sam')

print(w1.owner+" account:",w1.check_balance())
print(w2.owner+" account:",w2.check_balance())

#depositing money
w1.cash_in(500)
w2.cash_in(-100)

print(w1.owner+" account:",w1.check_balance())
print(w2.owner+" account:",w2.check_balance())

#sending money
w1.send_money(50,w2)


print(w1.owner+" account:",w1.check_balance())
print(w2.owner+" account:",w2.check_balance())

            
           