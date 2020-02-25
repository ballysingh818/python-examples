#!/usr/bin/env python3

import random

game = True

while game:

    player_decision = int(input("Please enter, 0 for Rock, 1 for Paper or 2 for Scissors: "))

    computer_decision = random.randint(0,2)

    if player_decision == computer_decision:
        print("Tie!")

    elif player_decision == 0 and computer_decision == 2:
        print("You win")
    
    elif player_decision == 1 and computer_decision == 0:
        print("You win")

    elif player_decision == 2 and computer_decision == 1:
        print("You win")

    else:
        print("You lose")

    do_you_want_to_continue = input("Do you want to continue? (y/n) ")
    
    if do_you_want_to_continue == "y":
        pass
    elif  do_you_want_to_continue == "n":
        print("Bye bye")
        game = False
    else:
        print("You did not put in a correct answer? So we will continue")