Selection ="H"
while Selection == "H":
    while True:
        try:
            print("\n --MENU:\n")
            print("H: Help")
            print("E: Exit")
            print("S: Start\n")
            Selection = str(input("Please make a selection from above: ")).upper()
            if Selection == "S" or Selection == "E" or Selection == "H":
                break
            else:
                print("\n *** Input not valid. Please enter one of the letters from the options above. ***")
        except:
            print("Input not valid. Please enter Letter from the options above.")

    if Selection == "H":
        print("\n\tThe goal of the game is to guess a RANDOM NUMBER before the computer does. After your first guess there will be a message in the console to let you know how close the initial guess was. Below are the options you can see with the fathest options at the top and the closer ones at the bottom:\n")
        print("\"Not even close. Guess again\" <- Furthest")
        print("\"You're cold\"")
        print("\"You're cool\"")
        print("\"You're warm\"")
        print("\"You're Hot\"")
        print("\"You're on fire\"")
        print("\"You're burning up\"")
        print("\"You're Right there\" <- Closest\n\n")
        print("After the initial guess you will only be told if your guess is closer (\"Getting warmer\") or if it's getting farther (\"Getting colder\"). While this will tell you how close you are getting you will not see if you have passed the number (EXAMPLE: if the RANDOM NUMBER is 20 and your previous guesses were 15 then 22, you will be notified wether you are gettin closer (\"Getting warmer\") but you will not be told if you passed the number).")
    elif Selection == "E":
        print("Exiting the game.")
    elif Selection == "S":

        import random

        ## Creates number to guess
        RandomNum=random.randrange(1,101)

        ## Initialization of initial variables ##
        UserGuesses = {}
        #ComGuesses = {}
        MyGuess=0
        counter = 0
        ComGuess = 0
        LowerLimit = 1
        UpperLimit = 101


        while MyGuess != RandomNum != ComGuess:
            ComGuess = random.randrange(LowerLimit,UpperLimit)
            #print(f"RandomNum: {RandomNum}")
            #ComGuesses[f"CompGuess{counter}"] = ComGuess
            #if counter == 0:
            if abs(ComGuess - RandomNum) >= 50:
                if ComGuess < 50:
                    #LRangeStart = max(35, ComGuess + 6)
                    LowerLimit = LowerLimit + random.randrange(max(35, max(ComGuess + 5,48)),49)
                elif ComGuess > 50:
                    #URangeStart = max(35,ComGuess + 6)
                    UpperLimit = UpperLimit - random.randrange(35,min(49,ComGuess + 5))
            else:
                UpperLimit = min((ComGuess + abs(ComGuess - RandomNum)) + 1,101)            
                LowerLimit = max(abs(ComGuess - abs(ComGuess - RandomNum)) - 1, 1)            

            while True:
                try:
                    MyGuess=int(input("\n\nEnter a whole number between 1 and 100: "))
                    if 0 < MyGuess <= 100:
                        counter += 1
                        break
                    else:
                        print("Number must be between 1 and 100.")
                except:
                    print("Input not valid. Please enter a whole number between 1 and 100")
            
            UserGuesses[f"UserGuess{counter}"] = MyGuess
            if len(UserGuesses) == 1:
                if (abs(MyGuess - RandomNum)) >= 50:
                    print("Not even close. Guess again")
                elif (abs(MyGuess - RandomNum)) < 50 and (abs(MyGuess - RandomNum)) >= 40:
                    print("You're cold")
                elif (abs(MyGuess - RandomNum)) < 40 and (abs(MyGuess - RandomNum)) >= 30:
                    print("You're cool")
                elif (abs(MyGuess - RandomNum)) < 30 and (abs(MyGuess - RandomNum)) >= 20:
                    print("You're warm")
                elif (abs(MyGuess - RandomNum)) < 20 and (abs(MyGuess - RandomNum)) >= 10:
                    print("You're Hot")
                elif (abs(MyGuess - RandomNum)) < 10 and (abs(MyGuess - RandomNum)) >= 5:
                    print("You're on fire")
                elif (abs(MyGuess - RandomNum)) < 5 and (abs(MyGuess - RandomNum)) >= 2:
                    print("You're burning up")
                elif (abs(MyGuess - RandomNum)) == 1:
                    print("You're Right there")
            elif len(UserGuesses) > 1:
                if (abs(UserGuesses.get(f"UserGuess{counter - 1}") - RandomNum)) > (abs(UserGuesses.get(f"UserGuess{counter}") - RandomNum)) and RandomNum != MyGuess:
                    print("Getting warmer")
                elif (abs(UserGuesses.get(f"UserGuess{counter - 1}") - RandomNum)) < (abs(UserGuesses.get(f"UserGuess{counter}") - RandomNum)):
                    print("Getting colder")
                elif (abs(UserGuesses.get(f"UserGuess{counter - 1}") - RandomNum)) == (abs(UserGuesses.get(f"UserGuess{counter}") - RandomNum)):
                    print("Same temperature")

        if MyGuess == RandomNum != ComGuess:
            print(f"GREAT GUESS!!! The number was {RandomNum}. Took you {counter} guesses.")
        elif ComGuess == RandomNum != MyGuess:
            print(f"YOU LOST. The computer won. The number was {RandomNum}. Took it {counter + 1} guesses.")
        elif MyGuess == RandomNum == ComGuess:
            print(f"YOU BOTH GUESSED CORRECTLY!!! The number was {RandomNum}. Took you all {counter} guesses.")


        print(f"\nLow is {LowerLimit}\n\n")
        print(f"High is {UpperLimit}\n\n")
        print(f"Computer guess is {ComGuess}\n")