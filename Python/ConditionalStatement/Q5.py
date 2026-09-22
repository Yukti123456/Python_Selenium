#Q5 - Check whether a number is divisible by 3 OR 5 but not both.
num = 15

if num % 3 == 0 and num % 5 == 0:
    print("InValid Number")
elif num % 5 == 0 or num % 3 == 0:
    print("VAlid Number")
