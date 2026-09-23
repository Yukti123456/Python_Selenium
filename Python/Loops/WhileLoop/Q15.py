# Q15 - Reverse a number using a while loop.
# Input: 12345
# Output: 54321
num = int(input("Enter a number: "))
reverse = 0
while num != 0:
    r = num % 10
    reverse = (reverse * 10) + r
    num =  num // 10
print(reverse)
