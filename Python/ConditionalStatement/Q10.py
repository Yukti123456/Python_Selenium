# 15. Coordinate Direction
#
# Given (x, y), determine the location:
#
# (0, 0) → Origin
# (0, y) → Y-axis
# (x, 0) → X-axis

x = int(input("Enter a Number: "))
y = int(input("Enter a Number: "))

match x,y:
    case _ if (x==0 and y==0):
        print("Origin")
    case _ if (x == 0 and y > 0):
        print("y-Axis")
    case _ if (x > 0 and y == 0):
        print("X-axis")
