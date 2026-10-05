#Q28 - 28. Check whether one string is a rotation of another.
# Input: "ABCD"
# Input: "CDAB"
#
# Output: True
word1 =  "ABCD"
word2 =  "CADB"
if len(word1) == len(word2) and word2 in word1+word1:
    print("String is a rotation of another string")
else:
    print("String is not a rotation of another string")
