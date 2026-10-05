#Q41 - Check whether a number is prime.

num = int(input("Enter a number: "))
isPrime = True
for i in range(2,num):
    if num%i == 0:
        isPrime = False
        break
    else:
        isPrime = True

if isPrime:
    print("Number is Prime")
else:
    print("Number is not Prime")