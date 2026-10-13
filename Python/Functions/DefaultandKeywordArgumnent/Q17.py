#Q16 - Calculate Power
# Create a function:
# power(number, exponent=2)
# Examples:
# power(5) → 25
# power(5, 3) → 125
def power(num,expo = 2):
    if expo == 0:
        return num
    else:
        return num ** expo
print(power(2,3))
print(power(5,2))