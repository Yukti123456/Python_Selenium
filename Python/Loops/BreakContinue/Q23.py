# Q23 - Keep taking numbers from the user. Stop when the user enters a negative number.
num = int(input("Enter a num: "))
while num:
    num = int(input("Enter a num: "))
    if  num < 0:
        break
