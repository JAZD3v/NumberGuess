import random

## Creates number to guess
MagicNumber=random.randrange(1,101)

## Initialization of initial variables ##
UserGuesses = {}
#ComGuesses = {}
MyGuess=0
counter = 0
ComGuess = 0
LowerLimit = 1
UpperLimit = 101


while MyGuess != MagicNumber != ComGuess:
    ComGuess = random.randrange(LowerLimit,UpperLimit)
    #ComGuesses[f"CompGuess{counter}"] = ComGuess
    #if counter == 0:
    if abs(ComGuess - MagicNumber) >= 50:
        if ComGuess < 50:
            #LRangeStart = max(35, ComGuess + 6)
            LowerLimit = LowerLimit + random.randrange(max(35, max(ComGuess + 5,48)),49)
        elif ComGuess > 50:
            #URangeStart = max(35,ComGuess + 6)
            UpperLimit = UpperLimit - random.randrange(35,min(49,ComGuess + 5))
    else:
        UpperLimit = min((ComGuess + abs(ComGuess - MagicNumber)) + 1,101)            
        LowerLimit = max(abs(ComGuess - abs(ComGuess - MagicNumber)) - 1, 1)            

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
        if (abs(MyGuess - MagicNumber)) >= 50:
            print("Not even close. Guess again")
        elif (abs(MyGuess - MagicNumber)) < 50 and (abs(MyGuess - MagicNumber)) >= 40:
            print("You're cold")
        elif (abs(MyGuess - MagicNumber)) < 40 and (abs(MyGuess - MagicNumber)) >= 30:
            print("You're cool")
        elif (abs(MyGuess - MagicNumber)) < 30 and (abs(MyGuess - MagicNumber)) >= 20:
            print("You're warm")
        elif (abs(MyGuess - MagicNumber)) < 20 and (abs(MyGuess - MagicNumber)) >= 10:
            print("You're Hot")
        elif (abs(MyGuess - MagicNumber)) < 10 and (abs(MyGuess - MagicNumber)) >= 5:
            print("You're on fire")
        elif (abs(MyGuess - MagicNumber)) < 5 and (abs(MyGuess - MagicNumber)) >= 2:
            print("You're Burning")
        elif (abs(MyGuess - MagicNumber)) == 1:
            print("You're Right there")
    elif len(UserGuesses) > 1:
        if (abs(UserGuesses.get(f"UserGuess{counter - 1}") - MagicNumber)) > (abs(UserGuesses.get(f"UserGuess{counter}") - MagicNumber)) and MagicNumber != MyGuess:
            print("Getting warmer")
        elif (abs(UserGuesses.get(f"UserGuess{counter - 1}") - MagicNumber)) < (abs(UserGuesses.get(f"UserGuess{counter}") - MagicNumber)):
            print("Getting colder")
        elif (abs(UserGuesses.get(f"UserGuess{counter - 1}") - MagicNumber)) == (abs(UserGuesses.get(f"UserGuess{counter}") - MagicNumber)):
            print("Same temperature")

if MyGuess == MagicNumber != ComGuess:
    print(f"GREAT GUESS!!! The number was {MagicNumber}. Took you {counter} guesses.")
elif ComGuess == MagicNumber != MyGuess:
    print(f"YOU LOST. The computer won. The number was {MagicNumber}. Took it {counter + 1} guesses.")
elif MyGuess == MagicNumber == ComGuess:
    print(f"YOU BOTH GUESSED CORRECTLY!!! The number was {MagicNumber}. Took you all {counter} guesses.")