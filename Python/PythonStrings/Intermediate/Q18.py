#Q18 - Find the longest word in a sentence.

sentence = "python is easy and python is powerful"
word = sentence.split()
max = float("-inf")
lon = ""
for i in word:
    if len(i) > max:
        max = len(i)
        lon = i
print(max,lon)

