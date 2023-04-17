array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

array2 = [" apple", "banana", "orange", "pear", "kiwi", "grape", "pineapple", "watermelon", "mango", "papaya"]

array3 = ["Lewis Hamilton", "Max Verstappen", "Valtteri Bottas", "Sergio Perez", "Lando Norris", "Charles Leclerc", "Carlos Sainz Jr.", "Daniel Ricciardo", "Esteban Ocon", "Fernando Alonso"]

array1Str = str(array1)
junction = []
for i in range(10):
    junction.append(array1[i])
    junction.append(array2[i])
    junction.append(array3[i])

print(junction)