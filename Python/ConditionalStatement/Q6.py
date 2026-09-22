# Q6 - Given three sides, determine whether a triangle is:
# Equilateral
# Isosceles
# Scalene

a = 90
b = 98
c = 46

if a == b == c:
    print("Euclidean Triangle ")
elif a == b or b == c or c == a:
    print("Isosceles Triangle ")
else:
    print("Scalene Triangle ")