#Q42 - Print all prime numbers between 1 and 100.
for i in range(2,100):
    isPrime = True
    for j in range(2,i-1):
       if i%j == 0:
         isPrime = False
         break
    if isPrime:
        print(i,end=", ")



