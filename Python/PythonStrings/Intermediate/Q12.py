#Q12 - 12. Find the first non-repeating character.
# Input: "aabbcdde"
# Output: "c"
input1 = "aabbcdde"
freq = {}
for i in input1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for i in input1:
    if freq[i] == 1:
        print(i)
        break
for i in freq: # this will gives keys in dicts
    print(i)
    print(freq[i]) # this will gives values in dicts