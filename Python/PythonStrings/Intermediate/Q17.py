#Q17 - 16. Count how many times each word occurs in a sentence.
# Input: "python is easy and python is powerful"
#
# Output:
# python: 2
# is: 2
# easy: 1
# and: 1
# powerful: 1
sentence = "python is easy and python is powerful"
word = sentence.split()
freq = {}
for i in word:
    if i in freq:
         freq[i] += 1
    else:
        freq[i] = 1
for i in word:
    print(i,"->",freq[i])



