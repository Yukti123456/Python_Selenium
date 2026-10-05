# Q25- Remove all occurrences of a given character from a string.
# Input: "programming"
# Remove: "r"
#
# Output: "pogamming"

word = "programming"
Remove = "r"
new = ""
for i in word:
    if i not in Remove:
        new = new + i

print(new)