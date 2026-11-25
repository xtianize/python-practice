#user login loop

password="python123"

def is_correct(pw):
    return pw.strip()==password
    return False

pw=input("Enter the password: ")    
while not is_correct(pw):
    pw=input("Wrong password, try again: ")
print("Access granted!")
    
    
    