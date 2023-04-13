countryA = 80000 ## 80.000
growthA = 1.03

countryB = 200000 ## 200.000 
growthB = 1.015

years = 0

while countryA < countryB:
    countryA = countryA * growthA
    countryB = countryB * growthB
    years += 1 ## years = years + 1

print(f"It will be need {years} years to country A overtake country B.")