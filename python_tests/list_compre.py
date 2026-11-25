#list comprehension and filtering scores

scores = [85, 62, 90, 74, 58, 95]
passed=[x for x in scores if x>=75]
try:
    print(sum(passed)/len(passed))
except ZeroDivisionError:
    print("The list should only contain number greater than zero")
