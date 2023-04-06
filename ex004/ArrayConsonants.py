array = ["I", "a", "m", "t", "h", "e", "g", "u", "y", "w"]
consonants = 0

for letter in array:
    if letter.isalpha() and letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
        consonants = consonants + 1

print('The quantidy of consonants in the array is:', consonants)