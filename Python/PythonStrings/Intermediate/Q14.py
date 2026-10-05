# Q14 - 14. Remove duplicate characters while preserving their original order.
# Input: "programming"
# Output: "progamin"
word = "programming"
new = ""
for i in word:
    if i not in new:
        new = new + i
    else:
        new = new

print(new)