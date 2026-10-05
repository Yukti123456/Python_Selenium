#Q15 - 15. Check whether two strings are anagrams.
# Input: "listen"
# Input: "silent"
#
# Output: True
word1 = input("Enter a word1: ")
word2 = input("Enter a word2: ")

if len(word1) == len(word2) and sorted(word1) == sorted(word2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")