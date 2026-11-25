#sum of all consecutive integers from n1 to n2
 
def consecutive_sum(n1,n2):
    n1=n1+n2
    n2=n2/2
    return n1*n2

n1=int(input("enter starting number:"))
n2=int(input("enter last number: "))

print(consecutive_sum(n1,n2))