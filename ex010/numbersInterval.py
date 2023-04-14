numList = []

## input and transforming the number into int and putting in a array
for num in range(2):
    numberInput = input(f"Enter number {num+1}: ")
    intNumber = int(numberInput)
    numList.append(intNumber)

## selecting the bigger and smallest number
maxNum = max(numList)
minNum = min(numList)

## creating a list that contains the smallest number to the bigger one
intervalList = list(range(minNum, maxNum + 1))

## getting the lenth of the array
lenIntervalList = len(intervalList)
## excluding the last number of the array
intervalList.pop(lenIntervalList - 1)

## deleting the first number of the array
intervalList.pop(0)

print(intervalList)