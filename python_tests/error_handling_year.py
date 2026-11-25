#error handling user age, output birth year
from datetime import date
try:
    user_age=int(input("Please enter your age: "))
    if user_age <0:
        raise ValueError
    birth_year= date.today().year-user_age
    print("You are born on year", birth_year)
    
except ValueError:
    print("Please enter a valid age")
