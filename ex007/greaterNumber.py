numbers = []

a = 1
i = 1
while a <= 5:
    numberInput = input(f"Enter the number {i}: ")
    numberInput = int(numberInput)
    numbers.append(numberInput)
    i += 1
    a += 1
    
greatherNum = max(numbers)
print(greatherNum)