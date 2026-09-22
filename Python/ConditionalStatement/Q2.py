# Login Validation
#
# Given:
#
# username = "admin"
# password = "1234"
#
# Take username and password as input and print "Login successful" only if both are correct.
username = input("Enter Username: ")
password = input("Enter Username: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid Username")
