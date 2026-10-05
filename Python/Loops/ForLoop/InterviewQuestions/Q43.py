#Q43 -- Find the largest number in a list without using max().
ele = [34,8,2,3,1,90]
max = -9999
for i in ele:
    if i > max:
        max = i
print(max)

