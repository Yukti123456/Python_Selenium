#Q19 - Find the shortest word in a sentence.

sentence = "python is a easy and python is powerful"
word = sentence.split()
min = float("inf")
short = ""
for i in word:
    if len(i) < min:
        min = len(i)
        short = i

print(short,min)
