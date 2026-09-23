#Q16 -- Find the sum of digits of a number.
# Input: 12345
# Output: 15

num = int(input("Enter a number: "))
sum = 0
while num != 0:
    r = num % 10
    sum = sum + r
    num = num //10
print(sum)