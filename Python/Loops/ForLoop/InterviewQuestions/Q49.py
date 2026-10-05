#Q49 - Find whether a number is an Armstrong number.
# Input: 153
# Output: Armstrong Number
num = int(input("Enter a number: "))
dup = num
count = 0
while dup > 0:
    r = dup % 10
    count += 1
    dup = dup // 10

print(count)

dup = num
sum = 0

while dup>0:
    r = dup % 10
    sum = sum + r ** count
    print(sum)
    dup = dup//10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


