#!/usr/bin/env python3
from functions import playerTurn
from functions import play
from functions import getPlayerLetter


exitFlag = False
playerLetter = ''
firstFlag = True

while(exitFlag == False):
    if(firstFlag == True):
        playerLetter = getPlayerLetter()
        play(playerLetter)
        firstFlag = False
    else:
        choice = ''
        while choice != 'a' and choice != 'b' and choice != 'c' and choice != 'A' and choice != 'B' and choice != 'C':
            choice = input("What do you want to do?\n\tA) Rematch\n\tB) Re-play\n\tC) Exit\n\n(a / b /c): ")
            if(choice == 'c' or choice == 'C'):
                exitFlag =  True
                break
            elif(choice == 'a' or choice == 'A'):
                if(playerLetter == 'X'):
                    playerLetter = 'O'
                elif(playerLetter == 'O'):
                    playerLetter ='X'
                else:
                    print("Something wetn wrong")
                    exit()
            elif(choice != 'b' and choice != 'B'):
                print("Invalid input. Try again...\n")
        if(exitFlag != True):
            play(playerLetter)
