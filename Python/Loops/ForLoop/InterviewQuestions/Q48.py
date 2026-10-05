#Q48 - Find the common elements between two lists using loops.
# List 1 = [1, 2, 3, 4, 5]
# List 2 = [3, 4, 5, 6, 7]
#
# Output:
# [3, 4, 5]

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
l3 = []
for i in l1:
    for j in l2:
        if i == j:
            l3.append(i)
print(l3)