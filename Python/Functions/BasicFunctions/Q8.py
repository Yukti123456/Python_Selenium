#8 - 8. Calculate Factorial
# Create a function factorial(n) that returns the factorial of n.
# factorial(5) → 120
def factorial(n):
    if n == 1:
        return 1

    else:
        return n * factorial(n-1)
print(factorial(4))