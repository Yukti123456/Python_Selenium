#Q2 -- Count the number of vowels and consonants in a string.
word = "Welcome to Jungle!"
vowels = 'aeiou'
count1 = 0
count2 = 0
for i in word:
    if i not in vowels:
        count1 += 1
    elif i in vowels:
        count2 +=1
print("Numbers of Vowels: ",count2)
print("Numbers of Consonants: ",count1)