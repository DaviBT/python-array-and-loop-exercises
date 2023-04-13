countryA = input("Enter the country A population: ")
growthA =  input("Enter the country A growth percentage (in decimal): ")

countryB = input("Enter the country B population: ")
growthB = input("Enter the country B growth percentage (in decimal): ")

while a < 0:
    countryA = input("Enter the country A population: ")
    if countryA < 1:
        print("Enter a valid number!")
    growthA =  input("Enter the country A growth percentage (in decimal): ")

    countryB = input("Enter the country B population: ")
    if countryB < 1:
        print("Enter a valid number!")
    growthB = input("Enter the country B growth percentage (in decimal): ")

years = 0
while countryA < countryB:
    countryA = countryA * growthA
    countryB = countryB * growthB
    years += 1

print(f"It will be need {years} to country A overtake country B.")