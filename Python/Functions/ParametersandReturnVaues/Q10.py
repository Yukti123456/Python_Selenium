#Q10 - 10. Find Largest of Three
# Create a function that accepts three numbers and returns the largest.
def largest(a,b,c):
    if b > a > c:
        return b
    elif a > b > c:
        return a
    else:
        return c
print(largest(78,90,34))