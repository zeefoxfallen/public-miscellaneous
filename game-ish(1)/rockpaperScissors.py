import random

set = ["rock", "paper", "scissors"]

computer = set[random.randint(0,2)]

player = input("rock, paper, scissors?")
if player == computer:
    print("tie to {}".format(computer))
elif player == "rock":
    if computer == "paper":
        print("you suck and lost to paper")
    else:
        print("you win and beat scissors")
elif player == "paper":
    if computer == "rock":
        print("you win and beat rock")
    else:
        print("you suck and lost to scissors")
elif player == "scissors":
    if computer == "paper":
        print("you win and beat paper")
    else:
        print("you suck and lost to rock")