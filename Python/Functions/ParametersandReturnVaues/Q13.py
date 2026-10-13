#Q13- 3. Palindrome Checker
# Create a function that checks whether a string is a palindrome.
# is_palindrome("madam") → True
# is_palindrome("hello") → False
def palindrome(s):
    dup =""
    for i in range(len(s)-1,-1,-1):
        dup +=s[i]
    if dup == s:
        return True
if palindrome("Hello"):
    print("Palindrome")
else:
    print("Not a palindrome")