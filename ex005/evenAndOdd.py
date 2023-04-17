numbers = [75, 11, 68, 97, 36, 56, 87, 1, 84, 55, 42, 20, 6, 76, 40, 64, 23, 32, 29, 83]

evenNumbers = [ ] ## par
oddNumbers = [ ] ## ímpar

for num in numbers:
    if num % 2  == 0:
        evenNumbers.append(num)
    else:
        oddNumbers.append(num)

print(f'The even numbers are {evenNumbers} and the odd numbers are are {oddNumbers}.')