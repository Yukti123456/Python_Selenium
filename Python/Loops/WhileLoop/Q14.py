# Q14 - Count the number of digits in an integer.
# Input: 123456
# Output: 6

num = int(input("Enter a number: "))
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print(count)

