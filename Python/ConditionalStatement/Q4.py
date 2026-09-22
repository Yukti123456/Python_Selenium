#Q4 - Triangle Validity
# Given three sides, check whether they can form a valid triangle.

a = 34
b = 67
c = 145

if a > 0 and b > 0 and c > 0:
   if a+b>c and a+c>b  and b + c > a:
      print("Valid triangle.")
   else:
      print("Not a valid triangle.")
