#Q17 -- Check whether a number is a palindrome.
# Input: 121
# Output: Palindrome

num = int(input("Enter a number: "))
reverse = 0
dup =0
num = dup
while num != 0:
    r = num % 10
    reverse = (reverse * 10) + r
    num = num //10
if (reverse == dup):
    print("Palindrome")
else:
    print("Not a Palidrome")