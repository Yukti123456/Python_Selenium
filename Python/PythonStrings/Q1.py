#Q1 -- Write a program to reverse a string without using [::-1].
word = "Hello"
reverse = ""
for i in range (len(word)-1,-1,-1):
    print(word[i],end ="")

for i in range (len(word)-1,-1,-1):
    reverse = reverse + word[i]
    
print(reverse)