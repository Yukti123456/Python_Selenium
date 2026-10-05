# Q31 -- Find the frequency of each character.
# Input: "hello"
#
# Output:
# h → 1
# e → 1
# l → 2
# o → 1

word = "hello"
frequency = {}
for i in word:
    if i in frequency:
        frequency[i]  += 1
    else:
        frequency[i] =  1
for char in frequency:
    print(char, "→", frequency[char])
