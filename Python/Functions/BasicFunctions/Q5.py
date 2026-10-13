# #Q5 - Even or Odd
# Create a function that accepts a number and returns whether it is "Even" or "Odd".
from operator import truediv

num = int(input("Enter a number: "))
def EvenOdd(num):
    if(num%2==0):
        return True
    else:
        return False
if(EvenOdd(num)):
    print("Even")
else:
    print("Odd")