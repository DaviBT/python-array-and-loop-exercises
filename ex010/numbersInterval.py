p = 0
while p < 1:
    numberInput = input("Enter a number: ")
    numberInput = int(numberInput)
    if numberInput < 1:
        print("Enter a number above 1!")
    else:
        print(f"The number {numberInput} is valid!")
        p = 1

g = 0
while g < 1:
    finalNumberInput = input("Enter another number: ")
    finalNumberInput = int(finalNumberInput)
    if finalNumberInput < 1:
        print("Enter a number above one.")
    elif numberInput > finalNumberInput:
        numberInput, finalNumberInput = finalNumberInput, numberInput
        g = 1
    else:
        print(f"The number {finalNumberInput} is valid!")
        g = 1

intervalNumbers = finalNumberInput - numberInput
print(intervalNumbers)
i = numberInput + 1
while i < numberInput:
    numberInput += 1
    print(numberInput)