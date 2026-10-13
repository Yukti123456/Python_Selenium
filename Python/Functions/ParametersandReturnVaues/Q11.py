#Q11 - 11. Count Vowels
# Create a function that accepts a string and returns the number of vowels.
# count_vowels("programming") → 3
def vowel(s):
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(vowel('helloiauee'))