#Q20 - Keep asking for a password until the user enters the correct password.
password = "admin12"

pass1 = input("Enter a password: ")
while pass1 != password:
    pass1 = input("Enter a password: ")
print("You Entered Correct Password!")