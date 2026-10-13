#Q14- 14. Count Digits
# Create a function that accepts an integer and returns the number of digits.
# count_digits(12345) → 5

def digitCount(num):
    count = 0
    while(num >0):
        r = num % 10
        count += 1
        num //= 10
    return count
print(digitCount(6373))