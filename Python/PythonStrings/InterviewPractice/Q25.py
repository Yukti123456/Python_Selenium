#Q25 - Find all duplicate characters in a string.
word = "Hello World"
new = ""
dup = ""
for i in word:
    if i in new:
        if i not in dup:
            dup = dup + i
            print(i,end=" ")
    else:
        new = new + i
