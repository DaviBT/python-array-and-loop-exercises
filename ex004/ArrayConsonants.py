array = ["I'm", "the", "guy", "who"]
consonants = 0

for letter in array:
    for letter in array:
        if letter.isalpha() and letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            consonants = consonants + 1

print('The quantidy of consonants in the array is:', consonants)