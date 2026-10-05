#Q20 = 18. Reverse each word in a sentence while keeping the word order unchanged.
# Input:  "I love Python"
# Output: "I evol nohtyP"
sentence = "I love Python"
word = sentence.split()
for char in word:
    for i in range(len(char)-1,-1,-1):
        print(char[i],end="")
    print(end=" ")
