#Q9 - Convert a string to uppercase without using .upper().
w = "hello"
new = ""
# ord() -> converts character → number
# chr() =  "converts the number back to a character:"
for i in w:
    if 'a' <= i <= 'z':
         new = new +  chr(ord(i) - 32)
    else:
        new = new + i
print(new)