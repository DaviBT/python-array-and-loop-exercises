while True:
   userInput = input("Enter your name: ")
   passwordInput = input("Enter your password: ")
   if userInput == passwordInput:
        print("Your username and password can't be the same!")
   else:
    print(f"Your username is {userInput} and your password is {passwordInput}")
    