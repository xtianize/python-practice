#calculate fare function
import math

def calculate_fare(km):
    base_fare=13
    km=math.floor(km)
    if km<=4:
        return base_fare
    add_fare=2*(km-4)
    total_fare=base_fare+add_fare
    return total_fare
    
user_trip=float(input("Enter total km: "))
print("Your total fare is ", calculate_fare(user_trip))