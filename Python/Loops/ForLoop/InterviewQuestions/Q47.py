#Q47 - Remove duplicate elements from a list using loops.
# Input:
# [1, 2, 2, 3, 4, 4, 5]
#
# Output:
# [1, 2, 3, 4, 5]
ele = [1, 2, 2, 3, 4, 4, 5]
#Approach 1 - without Loops
# s = set(ele)
# num = list(s)
# print(num)
#Approach 2 - with Loop
unique = []
for i in ele:
    if i not in unique:
        unique.append(i)
print(unique)
