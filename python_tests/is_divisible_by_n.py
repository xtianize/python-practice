# if divisible by 9
num=input("enter a number: ")
num=[int(n) for n in num]
if sum(num)%9==0:
    print("the number is divisible by 9")
else:
    print("the number is not divisible by 9")
    