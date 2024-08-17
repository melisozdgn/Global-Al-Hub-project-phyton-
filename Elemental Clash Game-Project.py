#Welcome Elemental Clash Game!
# Get ready for one of the most popular games in the world: Rock, Paper, Scissors, Water, Fire!
# The winner is determined by the first two rounds won. 
#The game consists of three outcomes:Player wins-Computer wins-Draw
# If both the player and the computer choose to replay after a round, the game will be repeated.
# Let's start the game and have fun!

import random

game_choices = ["Rock", "Paper", "Scissors", "Water", "Fire"]

# Win conditions 
win_conditions = {
    "Rock": {"Scissors", "Fire"},
    "Paper": {"Rock", "Water"},
    "Scissors": {"Paper", "Water"},
    "Water": {"Fire", "Rock"},
    "Fire": {"Scissors", "Paper"}
}

def play_rock_paper_scissors_water_fire_MELIS_OZDOGAN():
    while True:  
        player_wins = 0
        comp_wins = 0
        round_num = 0

        while player_wins < 2 and comp_wins < 2: 
            round_num += 1
            print(f"Round {round_num}")

            player_choice = input("Choose one (Rock, Paper, Scissors, Water, Fire): ").capitalize()
            
            while player_choice not in game_choices:
                print("Invalid choice. Please enter again,please.")
                player_choice = input("Choose one (Rock, Paper, Scissors, Water, Fire): ").capitalize()
            
            computer_choice = random.choice(game_choices)
            
            if player_choice == computer_choice:
                winner = 'Draw'
            elif computer_choice in win_conditions[player_choice]:
                winner = 'Player'
            else:
                winner = 'Computer'

            # Print choices
            print(f"Your choice: {player_choice}")
            print(f"Choice of computer: {computer_choice}")

            # Determine result
            if winner == 'Draw':
                print("It's a draw!")
            elif winner == 'Player':
                print("Congratulations, you win!")
                player_wins += 1
            else:
                print("Computer wins,sorry!")
                comp_wins += 1

            # Print score
            print(f"Score: Player {player_wins} - Computer {comp_wins}")

       
        if player_wins == 2:
            print("Congratulations, you won the game!")
        else:
            print("Sorry, computer won the game!")

        # Replay 
        play_again_player = input("Would you like to play again? (y/n): ")
        play_again_computer = random.choice(['y', 'n'])
        print(f"Choice of computer: {play_again_computer}")

        if play_again_player != 'y' and play_again_computer != 'y':
            print("Game over, come back later!")
            break  
        elif play_again_player == 'y' and play_again_computer == 'y':
            print("Let's start the game again!")
            continue  

play_rock_paper_scissors_water_fire_MELIS_OZDOGAN()
