#Q29 - Count digits and special characters in a string.
word = input("Enter a word:")
digit = 0
special = 0
for i in range(0, len(word)):
    if (word[i] >= 'a' and word[i] <= 'z'):
        pass
    elif (word[i] >= '0' and word[i] <= '9'):
        digit += 1
    else:
        special += 1
print(digit)
print(special)

#Approach 2
word = input("Enter a word: ")
digit = 0
special = 0

for i in range(len(word)):
    if word[i].isalpha():
        pass
    elif word[i].isdigit():
        digit += 1
    else:
        special += 1

print("Digits:", digit)
print("Special characters:", special)
