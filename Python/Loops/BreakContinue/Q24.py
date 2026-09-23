#Q24 - Search for a number in a list and stop the loop when you find it.
#numbers = [10, 25, 32, 45, 67, 89]
numbers = [10, 25, 32, 45, 67, 89]
num = int(input("Enter a number: "))
for i in range(len(numbers) + 1):
    if num == numbers[i]:
        print("Found at index", i)
        break


