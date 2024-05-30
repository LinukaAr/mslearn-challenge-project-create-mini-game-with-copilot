   
# create a multiplayer rock paper scissors game
#opponent and can randomly choose one of the elements (rock, paper, or scissors)
#user will be prompted to choose one of the elements using CLI
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The mini game must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random   
import os
import sys
def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    opponent_score = 0

    while True:
        # Prompt user for their choice
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        # Check if the player's choice is valid
        if player_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate opponent's choice
        opponent_choice = random.choice(options)

        # Determine the winner
        if player_choice == opponent_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
                (player_choice == 'paper' and opponent_choice == 'rock') or \
                (player_choice == 'scissors' and opponent_choice == 'paper'):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            opponent_score += 1

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    # Display the final scores
    print(f"Player score: {player_score}")
    print(f"Opponent score: {opponent_score}")

play_game()