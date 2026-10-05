#Q5 - Convert the first character of a string to uppercase without using .capitalize().
word = "hello"
new = ""
for i in range(len(word)):
    if i == 0 and word[i].islower():
        new = new +  word[i].upper()
    else:
        new = new + word[i]
print(new)
