#Q44 - Find the smallest number in a list without using min().
ele = [34,8,2,3,1,90]
min = float('inf')
for i in ele:
    if min > i:
        min = i
print(min)