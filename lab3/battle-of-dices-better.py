# Battle of Dices with different dice for each player
# Task 13 extended: using dice.py so each player can have their own die type.

from dice import roll_d6    # Player 1 will use d8, Player 2 will use d12

print("Welcome to Battle of Dices (different dice for each player)!")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
rounds = 0
TARGET_WINS = 3


# Game loop
while player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    rounds += 1
    print(f"\n--- Round {rounds} ---")

    # Player 1 rolls a d8, Player 2 rolls a d12
    player1_roll = roll_d8()
    print("Player 1 rolled (d8):", player1_roll)

    player2_roll = roll_d12()
    print("Player 2 rolled (d12):", player2_roll)

    # Decide who won the round
    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("Player 2 wins this round!")
    else:
        print("It's a tie — no points!")

    # Print current score
    print("The game score is Player 1", player1_wins, "vs.", player2_wins, "Player 2.")

# When loop ends, someone has won 3 rounds
if player1_wins == TARGET_WINS:
    print("\nPlayer 1 is the newest Battle of Dices Champion!")
else:
    print("\nPlayer 2 is the newest Battle of Dices Champion!")

print("Total rounds played:", rounds)