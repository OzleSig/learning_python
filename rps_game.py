import random

while True:
    choices = ["rock", "paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer =="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose! Loser.")
        if computer == "Scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You win! WINNER!")
    elif player == "scissors":
        if computer =="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You win!  WINNER!")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose! Loser.")
    elif player == "paper":
        if computer =="rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You win!  WINNER!")
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose! Loser.")
    
    play_again= input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")