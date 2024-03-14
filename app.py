import random
# create a console game that allows the user to play a game of rock, paper, scissors against the computer.The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.By the end of each round, the player can choose whether to play again.Display the player's score at the end of the game.The mini game must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice not in options:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)

        print(f"Player: {player_choice.capitalize()} vs Computer: {computer_choice.capitalize()}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You won!")
            player_score += 1
        else:
            print("You lost!")
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

play_game()

