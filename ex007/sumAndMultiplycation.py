numbers = []
num = 1
product = 1
NumbersSum = 1

while num <= 5:
    numbers.append(num)
    numbersSum = sum(numbers)
    for num in numbers:
        product *= num
    num += 1

NumbersSum = sum(numbers)
print("The product of the numbers inside the array is " + str(product))
print("The sum of the numbers inside the array is " + str(NumbersSum))
print(numbers)