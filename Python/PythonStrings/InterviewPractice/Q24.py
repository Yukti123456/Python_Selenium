#Q24 - 22. Separate letters, digits, and special characters.
# Input: "Py@123#thon!"
#
# Output:
# Letters: 6
# Digits: 3
# Special characters: 3

str = "Py@123#thon!"
digits = 0
letters = 0
Special = 0
for i in str:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
    else:
        Special += 1
print("Letters: ", letters)
print("Digits: ", digits)
print("Special: ", Special)

