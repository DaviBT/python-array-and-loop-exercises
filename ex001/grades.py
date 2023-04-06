grade = 0.0
gradesInput =  0.0

while True:
    inputMessage = input("Enter a grade between 0 and 1 of the student 1: ")
    inputMessageFloat = float(inputMessage)
    if inputMessageFloat < 0 or inputMessageFloat > 10:
        print("Enter a valid number!")
    else:
        print(f"Thank you, {inputMessageFloat} is a valid number.")
    break
