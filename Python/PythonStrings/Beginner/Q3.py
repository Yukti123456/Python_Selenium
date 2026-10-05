#Q3 - Count how many times a particular character occurs in a string.
word = "Hellolougbklmlml"

#Approach-1
count = 0
for char in word:
    if 'l' == char:
        count += 1
print(count)
#Approach-2
l = word.count('l')
print(l)