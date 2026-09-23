#Q22 - Print numbers from 1 to 20 but skip multiples of 3.
for i in range(20):
     if i % 3 == 0:
        continue
     print(i)