a = 0

while a == 0:
    ## name
    nameInput = input("Enter your name: ")
    nameLen = len(nameInput)
    if nameLen <= 3:
        print("Write a valid name!")
    else:
        print(f"{nameInput} is a valid Name.")
        a = 1    

while a != 2:
    ## age
    ageInput = input("Enter your age: ")
    ageInput = int(ageInput)
    if ageInput < 0 or ageInput > 150:
        print("Enter a valid age!")
    else:
        print(f"{ageInput} is a valid age")
        a = 2    
    
while a != 3:
    ## salary
    salaryInput = input("Enter your salary: ")
    salaryInput = int(salaryInput)
    if salaryInput < 0:
        print("Enter a valid number!")
    else:
        print(f"{salaryInput} is a valid salary")
        a = 3   
    
while a != 4:
    ## sex
    sexInput = input("Enter your sex (f or m): ")
    if sexInput != "f" or sexInput != "m":
        print("Enter a valid gender!")
    else: 
        print(f"{sexInput} is a valid gender.")
        a = 4    

while a != 5:
    ## civil state
    civilState = input("Enter your civil state (married, single, widower or divorced): ")
    if civilState != "married" or civilState != "single" or civilState != "windower" or civilState != "divorced":
        print("Enter a valid civil state!")
    else:
        print(f"{civilState} is a valid state.")
        a = 5    