#Q21 - 21. Reverse the order of words in a sentence.
# Input:  "I love Python"
# Output: "Python love I"
sentence = "I love Python"
word = sentence.split()
rev = word[::-1]
print(rev)
for i in range(len(word)-1,-1,-1):
         print(word[i],end=" ")

