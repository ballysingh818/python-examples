#!/usr/bin/env python3

import random

game = True

rock_counter = 0
paper_counter = 0
scissors_counter = 0

rps = ["Rock", "Paper", "Scissors"]

def computer_learning():
    counters = [rock_counter, paper_counter, scissors_counter]
    if rock_counter == max(counters):
        return 1
    if paper_counter == max(counters):
        return 2
    if scissors_counter == max(counters):
        return 0

while game:

    player_decision = int(input("Please enter, 0 for Rock, 1 for Paper or 2 for Scissors: "))

    computer_decision = computer_learning()

    if player_decision == computer_decision:
        print("Tie!")

    elif player_decision == 0 and computer_decision == 2:
        rock_counter +=1
        print("You win")
    
    elif player_decision == 1 and computer_decision == 0:
        paper_counter +=1
        print("You win")

    elif player_decision == 2 and computer_decision == 1:
        scissors_counter +=1
        print("You win")

    else:
        print("You lose")
    
    print("You chose: " + rps[player_decision] + " and the computer chose " + rps[computer_decision])

    do_you_want_to_continue = input("Do you want to continue? (y/n) ")
    
    if do_you_want_to_continue == "y":
        pass
    elif  do_you_want_to_continue == "n":
        print("Bye bye")
        game = False
    else:
        print("You did not put in a correct answer? So we will continue")
