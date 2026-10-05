#Q33 -- Find the first character that appears only once.

word = input("Enter Word: ")
fre = {}
for char in word:
    if char in fre:
        fre[char] += 1
    else:
        fre[char] = 1

for char in fre:
    if fre[char] == 1:
        print("The first character that appears only once: ",char)
        break