#Q11 - 11. Find the frequency of every character in a string.
# Example:
# Input:  "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
word = "hello"
freq = {}
for i in word:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)