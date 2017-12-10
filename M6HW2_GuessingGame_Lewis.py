# In this assignment, you will create a simple computer in Python
# 10/31/2017
# CTI-110 M6HW2 - Random Number Guessing Game
# Johnny Lewis

import random

def generateRandomNumber():
    randomNumber = random.randint( 1, 100 )
    return randomNumber

def askUserForNumber( message = "Guess the number: " ):
    userNumber = int( input( message ))
    return userNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return "Too high"
    elif userNumber < randomNumber:
        return "Too low"
    else:
        return  "Congratulations!"

def main():
    print()
    userCongratulated = False
    letsStart = True

    while userCongratulated or letsStart:
        userNumberOfGuesses = 0
        randomNumber = generateRandomNumber()
        # print( "For testing purposes, random number: ", randomNumber )
        userNumber = askUserForNumber()
        userNumberOfGuesses += 1
        message = checkUserNumber( userNumber, randomNumber )

        while message != "Congratulations!":
            print( message )
            userNumber = askUserForNumber( "Try again: " )
            userNumberOfGuesses = userNumberOfGuesses + 1
            message = checkUserNumber( userNumber, randomNumber )

        print()
        print( message, "It took you", userNumberOfGuesses,\
               " attempts to guess correctly\n" ) 
        userCongratulated = True

main()
        

    
    
   
