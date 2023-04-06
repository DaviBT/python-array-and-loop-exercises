a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

aSum = 0
for num in a:
    squaredNumbers = num * num
    aSum = squaredNumbers + aSum
print(aSum)