x = int(input("Enter a value of x: "))

match x:
    case 0:
        print("Value is 0")
    case 4 if x% 2!=0:
        print("value is 4")
    case _ if x!=89:
        print("Value is not a number")