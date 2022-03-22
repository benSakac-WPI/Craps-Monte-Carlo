#Module with function to play one game of craps and supporting functions
#Author: Ben Sakac <bisakac>


#Global variable list
playerWins = None
initialRoll = 0
numRolls = 0


#Function simulates playing one game of craps and 
#returns the result and number of rolls to terminate the game
def playOneGame():
    global playerWins, numRolls
    firstRound()
    if playerWins is None:
        while playerWins is None:
            rFp = rollDice()
            numRolls += 1
            if rFp == initialRoll:
                playerWins = True
            elif rFp == 7:
                playerWins = False
    return(playerWins, numRolls)


#Function to simulate the first round of a game of craps 
def firstRound():
    global playerWins, numRolls, initialRoll
    playerWins = None
    initialRoll = rollDice()
    numRolls = 1
    if initialRoll == 7 or initialRoll == 11:
        playerWins = True
        return(initialRoll, playerWins, numRolls)
    elif initialRoll == 2 or initialRoll == 3 or initialRoll == 12:
        playerWins = False
        return(initialRoll, playerWins, numRolls)
    else:
        return(initialRoll, playerWins, numRolls)
    


#Function simulates roll of two dice
def rollDice():
        from random import randint
        d1 = randint(1, 6)
        d2 = randint (1, 6)
        roll = d1 + d2
        #For debugging purposes 
        #print("D1 is {} and D2 is {}, sum is {}".format(d1, d2, roll))
        return(roll)
