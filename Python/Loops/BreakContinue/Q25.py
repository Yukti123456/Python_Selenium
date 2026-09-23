#Q25 - Print numbers from 1 to 50, but:
# Skip even numbers.
# Stop when the number reaches 35.
i = 1

while i <=50 :

    if i % 2 == 0:
        i = i + 1
        continue
    print(i)
    if i == 35:
        break
    i = i + 1
