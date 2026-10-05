#Q29 - Find the number of substrings in a string.

word = "abc"
#Approch-1
# sub = int((len(word)*(len(word)+1))/2)
# print(sub)
#Approch-2
count = 0
for i in range(len(word)):
    for j in range(i+1,len(word)+1):
        print(word[i:j])
        count+=1
print(count)
