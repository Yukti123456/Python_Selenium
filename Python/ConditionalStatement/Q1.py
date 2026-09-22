# Q1 - Day of the Week
# Take a number from 1–7 and print the corresponding day.

day = int(input("Enter a number: "))

if day > 0:
    if day == 1:
        print("Day is Sunday")
    elif day == 2:
        print("Day is Monday")
    elif day == 3:
        print("Day is Tuesday")
    elif day == 4:
        print("Day is Wednesday")
    elif day == 5:
        print("Day is Thrussday")
    elif day == 6:
        print("Day is Friday")
    else:
       print("Day is Saturay")
else:
    print("Invalid User")