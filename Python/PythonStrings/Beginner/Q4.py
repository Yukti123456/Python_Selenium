#Q4 - Check whether a string is a palindrome.
word = input("Enter a word: ")
# Approach - 1
# new = ""
# for i in range(len(word)-1,-1,-1):
#     new = new + word[i]
# print("\n")
#
# if new == word:
#     print("The word is palindrome")
# else:
#     print("The word is not palindrome")
# Approach - 1
if word == word[::-1]:
    print("The word is palindrome")
else:
    print("The word is not palindrome")
