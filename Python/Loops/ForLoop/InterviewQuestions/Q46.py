#Q46 - Count how many times a particular number occurs in a list without using .count().
ele = [34,8,2,3,1,90,34,78,34]
num = int(input("Enter a number: "))
count = 0
for i in ele:
        if num == i:
            count += 1
print(count)