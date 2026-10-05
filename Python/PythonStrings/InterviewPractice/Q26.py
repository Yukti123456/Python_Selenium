#Q26 - Find the character with the second-highest frequency.
word = "HiHiIIIHelloNamaste"
freq = {}
max = float('-inf')
for i in word.lower():
    if i in freq:
        freq[i] = freq[i] + 1
    else:
       freq[i] = 1
for i in word.lower():
    if freq[i] > max:
        max = freq[i]

#print(max)
sec =  0
for i in freq:
    if max > freq[i] > sec:
        sec = freq[i]
        print("Second-highest frequency character:",i)
