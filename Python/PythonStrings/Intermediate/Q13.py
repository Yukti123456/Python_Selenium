#Q13 - 13. Find the first repeating character.
# Input: "python"
# Output: "None"
#
# Input: "programming"
# Output: "r"
#Approach -1
input1 = "programming"
freq = {}
for i in input1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
found = False

for i in input1:
    if freq[i] > 1:
        print("First repeating character:", i)
        found = True
        break

if not found:
    print("None")
# #Approach -2
input1 = "programming"

for i in range(len(input1)):
    for j in range(i + 1, len(input1)):
        if input1[i] == input1[j]:
            print("First repeating character:", input1[i])
            break
    else:
        continue
    break



