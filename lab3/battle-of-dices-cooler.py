# Battle of Dices - Cooler Edition
# In this version, each player rolls two different dice
# and the sum decides who wins the round.

from dice import roll_d8, roll_d12   # you can pick other dice too

print("Welcome to Battle of Dices - COOLER EDITION!")

player1_wins = 0
player2_wins = 0
rounds = 0
TARGET_WINS = 3

while player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    rounds += 1
    print(f"\n--- Round {rounds} ---")

    # Player 1 rolls a d8 and a d12
    p1_die1 = roll_d8()
    p1_die2 = roll_d12()
    player1_total = p1_die1 + p1_die2
    print("Player 1 rolled:", p1_die1, "and", p1_die2, "=> total:", player1_total)

    # Player 2 rolls a d8 and a d12
    p2_die1 = roll_d8()
    p2_die2 = roll_d12()
    player2_total = p2_die1 + p2_die2
    print("Player 2 rolled:", p2_die1, "and", p2_die2, "=> total:", player2_total)

    # Decide who won
    if player1_total > player2_total:
        player1_wins += 1
        print("Player 1 wins this round!")
    elif player2_total > player1_total:
        player2_wins += 1
        print("Player 2 wins this round!")
    else:
        print("It's a tie — no points!")

    print("The game score is Player 1", player1_wins, "vs.", player2_wins, "Player 2.")

# End of game
if player1_wins == TARGET_WINS:
    print("\nPlayer 1 is the Battle of Dices Champion!")
else:
    print("\nPlayer 2 is the Battle of Dices Champion!")

print("Total rounds played:", rounds)