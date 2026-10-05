#Q50 - 50. Print the Fibonacci series.
# Input: 10
#
# Output:
# 0 1 1 2 3 5 8 13 21 34
num = int(input("Enter the number: "))
f1 = 0
f2 = 1
for i in range(1,num + 1):
    if i ==1:
        print(f1,end=" ")
    elif i == 2:
        print(f2,end=" ")
    else:
        f3 = f1 + f2
        print(f3,end=" ")
        f1 = f2
        f2 = f3