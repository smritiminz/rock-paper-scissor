from rps import get_computer_choice, get_winner

print("🎮 Welcome to Rock-Paper-Scissors!")

while True:
    player = input("Choose rock, paper, or scissors (or type 'exit'): ").lower()
    if player == "exit":
        print("Thanks for playing!")
        break
    if player not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        continue

    computer = get_computer_choice()
    print(f"Computer chose: {computer}")

    winner = get_winner(player, computer)
    if winner == "draw":
        print("It's a draw!")
    elif winner == "player":
        print("🎉 You win!")
    else:
        print("😢 You lose!")
