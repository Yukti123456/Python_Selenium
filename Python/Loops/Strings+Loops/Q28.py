#Q28 - Count the number of uppercase and lowercase characters.
word = input("Enter a word:")
lower = 0
upper = 0
for i in range(0, len(word)):
    if word[i] >= 'a' and word[i] <= 'z':
        lower = lower + 1
    else:
        upper = upper + 1
print(lower)
print(upper)

#Approach 2

word = input("Enter a word:")
lower = 0
upper = 0
for i in range(0, len(word)):
    if word[i].islower():
        lower = lower + 1
    else:
        upper = upper + 1
print(lower)
print(upper)
