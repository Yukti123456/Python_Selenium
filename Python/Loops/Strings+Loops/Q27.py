#Q27 - Count vowels and consonants separately.

vowel = 0
consonants = 0
word = input("Enter a word:")
for i in range(0, len(word)):
    if word[i] in "aeiou":
        vowel = vowel + 1
    else:
        consonants = consonants + 1

print(vowel)
print(consonants)