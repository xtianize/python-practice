#mini e-wallet

balance=500.00
#1. Check Balance, 2. Cash In, 3. Send Money (preventing overdrafts if balance is too low), or 4. Exit.
def process_user(func):
    try:
        amt=float(input("enter desired amount: "))
        if amt<=0:
            print("Transaction failed.Invalid amount")
            print("Your current balance is",balance)
        else:
            print("Your current balance is",func(amt))
    except ValueError:
        print("Transaction failed.Invalid amount")
        print("Your current balance is",balance)
    
def cash_in(amt):
    global balance
    balance+=amt
    print("Transaction successful. Amount added:",amt)
    return balance
    
def send_money(amt):
    global balance
    if amt>balance:
        print("Transaction failed.You do not have enough balance.")
        return balance
    else:
        balance-=amt
        print("Transaction successful. Amount sent:",amt)
    return balance
    
def get_bal():
    return balance
    

while True:
    try:
        print("Please choose a number from the following menu: \n 1. Check Balance \n 2. Cash In \n 3. Send Money  \n 4. Exit")
        task=int(input("Hello, user! What can  I do for you?"))
    
        if task==4:
            print("Goodbye user! Thank you for banking.")
            break
        elif task==3:
            process_user(send_money)
        elif task==2:
            process_user(cash_in)
        elif task==1:
            print("Your current balance is", get_bal())
        else:
            print("Invalid request, please try again.")
    except ValueError:
        print("Invalid request, please try again.")
    is_repeating=input("Do you need anything else? [Y/N] ").upper()
    if is_repeating == 'N':
        print("Goodbye user! Thank you for banking.")
        break
    
    
        