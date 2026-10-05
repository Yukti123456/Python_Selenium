#Q23 - Check whether a string contains only alphabets without using .isalpha().
str = input("Enter a string: ")
alpha = False
for i in str:
    if not "a" <= i <= "z":
        alpha = False
        break
    else:
        alpha = True
if alpha:
    print("String contains only alphabets.")
else:
    print("String does not contain alphabets.")