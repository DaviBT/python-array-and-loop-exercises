array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

array2 = [" apple", "banana", "orange", "pear", "kiwi", "grape", "pineapple", "watermelon", "mango", "papaya"]

array1Str = str(array1)
junction = []
for i in range(10):
    junction.append(array1[i])
    junction.append(array2[i])

print(junction)