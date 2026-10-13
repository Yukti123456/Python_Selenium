#Q12 - 12. Reverse a String
# Create a function that accepts a string and returns its reverse.
# Don't use [::-1].
def reverse(s):
    for i in range(len(s)-1,-1,-1):
        print(s[i],end="")
reverse("Hello")
