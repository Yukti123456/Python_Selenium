# Q32 - Find all duplicate characters in a string.


word = input("Enter Word: ")
fre = {}

for char in word:
    if char in fre:
        fre[char] += 1
    else:
        fre[char] = 1
count = 0
for char in fre:
    if fre[char] > 1:
        print(char)
        count += 1
print("Totla number of duplicates in Strings are: ",count)
