#!/usr/bin/env python3

import random
from CalculatePosition import *
from Dial import Dial 
from GameBoard import * 
from HiddenTreasures import *
from Movement import *
from Navigation import * 
from PlayerPosition import *
from Trap import *
from TreasurePosition import *


def main():

    viewing = None
    option = None
    toGo = None
    toGoCondition = True
    playerXPosition = None
    playerYPosition = None
    treasureXPosition = None
    treasureYPosition = None
    hiddenXPosition = None
    hiddenYPosition = None
    trapX = None
    trapY = None
    con = True
    positionMatching = True

    while con:
        print("You awaken to find yourself in a barren moor. Try \"look\"")
        viewing = input().lower()

        if viewing == "look":
            print("Grey foggy clouds float oppressively close to you,\n" +
                        "reflected in the murky grey water which reaches up your\n" +
                        "shins.\n" +
                        "Some black plants barely poke out of the shallow water.")
            con = False
        else:
            print("You have entered an incorrect statement, \n" +
                        "do you wish to exit the viewing?, \n" +
                        "Please enter either \"Yes\" or \"No\"")

            option = input().lower()

            if option == "yes":
                con = False

            else:
                pass

    playerPosition = PlayerPosition()
    treasurePosition = TreasurePosition()
    hiddenTreasures = HiddenTreasures()
    trap = Trap()

    playerXPosition = playerPosition.calculateXPosition()
    playerYPosition = playerPosition.calculateYPosition()
    treasureXPosition = treasurePosition.calculateXPosition()
    treasureYPosition = treasurePosition.calculateYPosition()
    hiddenTXPosition = hiddenTreasures.calculateXPosition()
    hiddenTYPosition = hiddenTreasures.calculateYPosition()
    trapX = trap.calculateXPosition()
    trapY = trap.calculateYPosition()


    while positionMatching:
        
        if (playerXPosition == treasureXPosition or playerYPosition == treasureYPosition 
        or hiddenTXPosition == playerXPosition or hiddenTYPosition == playerYPosition 
        or hiddenTXPosition == treasureXPosition or hiddenTYPosition == treasureYPosition 
        or trapX == playerXPosition or trapY == playerYPosition):
            
            playerXPosition = playerPosition.calculateXPosition()
            playerYPosition = playerPosition.calculateYPosition()
            treasureXPosition = treasurePosition.calculateXPosition()
            treasureYPosition = treasurePosition.calculateYPosition()
            hiddenTXPosition = hiddenTreasures.calculateXPosition()
            hiddenTYPosition = hiddenTreasures.calculateYPosition()
            trapX = trap.calculateXPosition()
            trapY = trap.calculateYPosition()

        else:
            positionMatching = False

    navigation = Navigation(playerXPosition, playerYPosition, treasureXPosition, treasureYPosition)

    dial = Dial()

    print("The dial reads " + str(navigation.calculateResultant()) + "m")

    print("Try \"North\", \"South\", \"East\" or \"West\" \n" +
                "You notice a small watch-like device in your left hand.\n" +
                "It has hands like a watch, but the hands don’t seem to tell\n" +
                "time.")

    while toGoCondition:

        if playerXPosition == hiddenTXPosition and playerYPosition == hiddenTYPosition:
            print("You have discovered the legendary EI sword to aid you in your quest")
        
        if trapX == playerXPosition and trapY == playerYPosition:
            print("You fell into a trap, you're dead now")
            toGoCondition = False

        if playerXPosition == treasureXPosition and playerYPosition == treasureYPosition:
            print("You found the treasure, now go save the world. THE END")
            toGoCondition = False
        
        else:
            
            toGo = input("Please enter directions to go: ").lower()

            if toGo == "north" or toGo == "n":
                playerYPosition = dial.north(playerYPosition)
                navigation.setpY(playerYPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
            elif toGo == "east" or toGo == "e":
                playerXPosition = dial.east(playerXPosition)
                navigation.setpX(playerXPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
            elif toGo == "south" or toGo == "s":
                playerYPosition = dial.south(playerYPosition)
                navigation.setpY(playerYPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
            elif toGo == "west" or toGo == "w":
                playerXPosition = dial.west(playerXPosition)
                navigation.setpX(playerXPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
            else:
                print("You havent chosen a direction to go")
                print(navigation.calculateResultant())
            
if __name__ == "__main__":
    main()









