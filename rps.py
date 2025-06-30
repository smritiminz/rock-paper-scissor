import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"
