countryA = input("Enter the country A population: ")
growthA =  input("Enter the country A growth percentage (in decimal): ")

countryB = input("Enter the country B population: ")
growthB = input("Enter the country B growth percentage (in decimal): ")

a = 0
while a == 0:
    countryA = input("Enter the country A population: ")
    countryA = float(countryA)
    if countryA < 1:
        print("Enter a valid number!")
    else:
        a = 1

while a == 1:
    growthA =  input("Enter the country A growth percentage (in decimal): ")
    growthA = float(growthA)
    if growthA < 1.0:
        print("Enter a valid number!")
    else:
        a = 2

while a == 2:
    countryB = input("Enter the country B population: ")
    countryB = float(countryB)
    if countryB < 1:
        print("Enter a valid number!")
    else:
        a = 3
    
while a == 3:
    growthB = input("Enter the country B growth percentage (in decimal): ")
    growthB = float(growthB)
    if growthB < 1.0:
        print("Enter a valid number!")
    else:
        a = 4

years = 0
while countryA < countryB:
    countryA = countryA * growthA
    countryB = countryB * growthB
    years += 1

print(f"It will be need {years} to country A overtake country B.")