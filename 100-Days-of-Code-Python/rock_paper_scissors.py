# Rock, Paper, Scissors Game.
player_choice = ""
player_wins = 0
comp_wins = 0
import random

print("\nWelcome to Rock, Paper, Scissors. Type EXIT to end match\n")
while player_choice.upper() != "EXIT":
    random_number=random.randint(1,3)
    if random_number == 1:
        comp_choice = "ROCK"
    elif random_number == 2:
        comp_choice = "PAPER"
    else:
        comp_choice = "SCISSORS"

    player_choice = input("Choose your weapon! (Rock, Paper or Scissors?)\n ")

    if player_choice.upper() == comp_choice:
        print(f"Tied Game! Computer chose {comp_choice}")
    if player_choice.upper() == "ROCK" and comp_choice == "PAPER":
        print(f"Computer Wins! Computer chose {comp_choice}")
        comp_wins += 1
    if player_choice.upper() == "ROCK" and comp_choice == "SCISSORS":
        print(f"You Win! Computer chose {comp_choice}")
        player_wins += 1
    if player_choice.upper() == "PAPER" and comp_choice == "ROCK":
        print(f"You Win! Computer chose {comp_choice}")
        player_wins += 1
    if player_choice.upper() == "PAPER" and comp_choice == "SCISSORS":
        print(f"Computer Wins! Computer chose {comp_choice}")
        comp_wins += 1
    if player_choice.upper() == "SCISSORS" and comp_choice == "ROCK":
        print(f"Computer Wins! Computer chose {comp_choice}")
        comp_wins += 1
    if player_choice.upper() == "SCISSORS" and comp_choice == "PAPER":
        print(f"You Win! Computer chose {comp_choice}")
        player_wins += 1

print(f"\n\tPlayer Wins: {player_wins}\n\tComputer Wins: {comp_wins}")