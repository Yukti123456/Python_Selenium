#Q30 - Reverse a string using a loop without using [::-1].
word = "Hello"

for i in range(len(word)-1,-1,-1):
    print(word[i])