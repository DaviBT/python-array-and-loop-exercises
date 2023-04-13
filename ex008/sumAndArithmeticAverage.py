numbers = []
n = 1
i = 1
while i <= 5:
    num = input(f"Enter a number {n}: ")
    num = int(num)
    numbers.append(num)
    n += 1
    i += 1

sumNumbers = sum(numbers)
lenNumbers = len(numbers)
arithmeticAverage = sumNumbers / lenNumbers
print(arithmeticAverage)