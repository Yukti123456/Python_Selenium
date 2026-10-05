#Q22 - Check whether a string contains only digits without using .isdigit().
str = input("Enter a string: ")
digit = False
for i in str:
    if not  "0" <= i  <= "9":
        digit = False
        break
    else:
        digit = True
if digit:
    print("String contains only digits")
else:
    print("String does not contain digits")