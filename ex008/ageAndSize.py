ages = []
heights = []

for i in range(5):
    age = input("Enter the age form the person {}: ".format(i+1))
    age = int(age)
    height = input("Enter the height from the person {} in meters: ".format(i+1))
    height = float(height)
    ages.append(age)
    heights.append(height)

ages = list(reversed(ages))
ages = str(ages)
heights = list(reversed(heights))
heights = str(heights)

print("age reversed: " + ages)

print("height reversed:  " + heights)