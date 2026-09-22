num = int(input("Enter a Number: "))

if num < 0:
    print("Number is Negative")
elif num > 0:
    if num %2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number id Zero")