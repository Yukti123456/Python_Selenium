#Q16 - Find the most frequent character in a string.
word = "programmingmniimm"
freq =  {}
#Approach 1
for i in word:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

max = float("-inf")
max_char = ""
for i in word:
    if freq[i] > max:
        max = freq[i]
        max_char = i
print(max,max_char)
# Approach - 2
max_freq = 0
max_char = ""

for i in word:
    count = word.count(i)

    if count > max_freq:
        max_freq = count
        max_char = i

print(max_char, max_freq)