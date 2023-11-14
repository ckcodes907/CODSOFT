import random

def get_user_input():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_random_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_round_winner(player_input, computer_input):
    if player_input == computer_input:
        return "It's a tie!"
    elif (
        (player_input == "rock" and computer_input == "scissors") or
        (player_input == "scissors" and computer_input == "paper") or
        (player_input == "paper" and computer_input == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

user_score = 0
computer_score = 0

while True:
    user_input = get_user_input()
    computer_input = get_random_choice()

    print(f"You chose {user_input}. Computer chose {computer_input}.")

    result = determine_round_winner(user_input, computer_input)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Score - You: {user_score}, Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")
