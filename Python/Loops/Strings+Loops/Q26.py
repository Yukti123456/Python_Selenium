# Q26 - Count the number of vowels in a string.
# Input: "programming"
# Output: 3
vowel = 0
word = input("Enter a word:")
for i in range(0, len(word)):
    if word[i] in "aeiou":
        vowel = vowel + 1

print(vowel)