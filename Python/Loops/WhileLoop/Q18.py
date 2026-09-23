# Q18 -- Find the factorial of a number.
# Input: 5
# Output: 120

num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -=1
print(factorial)