#Q3 -- Find the second-largest of three numbers using conditional statements.

a = 8
b = 10
c = 67
if (a>b  and a<c) or (a <b and a > c):
    print("a is seocnd highes")
elif (a<b and b<c) or (a>b and b>c):
    print("b is seocnd highest")
else:
    print("c is seocnd highest")

