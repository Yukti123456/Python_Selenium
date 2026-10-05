#Q45 - Find the second-largest number in a list.
ele = [34,8,2,3,1,90]
#Approach -1
# s = set(ele)
# s = sorted(s)
# print(s[-2])
#Approach - 2
# ele.sort()
# ele.remove(ele[-1])
# print(ele[-1])
#Approach - 3
larg = float('-inf')
sec =  float('-inf')

for i in ele:
    if i > larg:
        sec = larg
        larg = i
    elif i > sec:
        sec = i
print(sec)