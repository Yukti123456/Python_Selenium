#Q30 - 29. Find the longest substring without repeating characters.
# Input: "abcabcbb"
# Output: "abc"
word = "abcabcbb"
max = float('-inf')
long = ""
for i in range(len(word)):
    for j in range(i+1,len(word)+1):
        sub = word[i:j]
        if len(word[i:j]) == len(set(word[i:j])):
            if len(word[i:j]) >= max:
                  max = len(sub)
                  long = sub
print(len(word))
print(max,long)
