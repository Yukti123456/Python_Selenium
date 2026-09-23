# Q13 - Find the sum of numbers from 1 to n.
# Input: 5
# Output: 15
num = int(input("Enter a number: "))
sum = 0
i = 0
while i <= num:
    sum = sum + i
    i= i+1

print(sum)
