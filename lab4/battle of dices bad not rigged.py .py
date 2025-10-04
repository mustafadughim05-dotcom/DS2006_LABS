# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

print("🎲 Welcome to Battle of Dices! 🎲")

player1_rolls = [random.randint(1, 6) for _ in range(6)]
player2_rolls = [random.randint(1, 6) for _ in range(6)]

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Battle of Dices - BAD VERSION 
# This version runs without any loops - just copying code multiple times


# Variables to store each roll separately
# player1_round1_roll = random.randint(1, 6)
# player2_round1_roll = random.randint(1, 6)
# player1_round2_roll = random.randint(1, 6)
# player2_round2_roll = random.randint(1, 6)
# player1_round3_roll = random.randint(1, 6)
# player2_round3_roll = random.randint(1, 6)
# player1_round4_roll = random.randint(1, 6)
# player2_round4_roll = random.randint(1, 6)
# player1_round5_roll = random.randint(1, 6)
# player2_round5_roll = random.randint(1, 6)
# player1_round6_roll = random.randint(1, 6)
# player2_round6_roll = random.randint(1, 6)


import random

print("🎲 Welcome to Battle of Dices! 🎲")
print("Playing with D20 dice!")

# Variables to keep track of the score:
print("Player 1 rolled: ", player1_rolls[0])
print("Player 2 rolled: ", player2_rolls[0])


# Round 1
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_rolls[0])
print("Player 2 rolled: ", player2_rolls[0])

input("\nPress ENTER to continue...")

if player1_rolls[0] > player2_rolls[0]:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_rolls[0], " is greater than ", player2_rolls[0])
elif player1_rolls[0] == player2_rolls[0]:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_rolls[0], " is greater than ", player1_rolls[0])

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

# Round 2
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_rolls[1])
print("Player 2 rolled: ", player2_rolls[1])

input("\nPress ENTER to continue...")

if player1_rolls[1] > player2_rolls[1]:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_rolls[1], " is greater than ", player2_rolls[1])
elif player1_rolls[1] == player2_rolls[1]:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_rolls[1], " is greater than ", player1_rolls[1])

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

# Round 3
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_rolls[2])
print("Player 2 rolled: ", player2_rolls[2])

input("\nPress ENTER to continue...")

if player1_rolls[2] > player2_rolls[2]:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_rolls[2], " is greater than ", player2_rolls[2])
elif player1_rolls[2] == player2_rolls[2]:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_rolls[2], " is greater than ", player1_rolls[2])

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

# Round 4
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_rolls[3])
print("Player 2 rolled: ", player2_rolls[3])

input("\nPress ENTER to continue...")

if player1_rolls[3] > player2_rolls[3]:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_rolls[3], " is greater than ", player2_rolls[3])
elif player1_rolls[3] == player2_rolls[3]:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_rolls[3], " is greater than ", player1_rolls[3])

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

# Round 5
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_rolls[4])
print("Player 2 rolled: ", player2_rolls[4])

input("\nPress ENTER to continue...")

if player1_rolls[4] > player2_rolls[4]:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_rolls[4], " is greater than ", player2_rolls[4])
elif player1_rolls[4] == player2_rolls[4]:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_rolls[4], " is greater than ", player1_rolls[4])

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

# Round 6
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_rolls[5])
print("Player 2 rolled: ", player2_rolls[5])

input("\nPress ENTER to continue...")

if player1_rolls[5] > player2_rolls[5]:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_rolls[5], " is greater than ", player2_rolls[5])
elif player1_rolls[5] == player2_rolls[5]:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_rolls[5], " is greater than ", player1_rolls[5])

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

print("\nGame over! (Maximum 6 rounds played)")


# Show game summary table
from tabulate import tabulate

print("\n" + "="*50)
print("GAME SUMMARY")
print("="*50)

# Dice label
dice_label = "D6"

# Create data for the tablemydata = # Build table rows from the lists
mydata = []
for i in range(len(player1_rolls)):
    mydata.append(("Player 1", f"Round {i+1}", str(player1_rolls[i]), dice_label))
    mydata.append(("Player 2", f"Round {i+1}", str(player2_rolls[i]), dice_label))

headers = ["Player", "Round", "Roll", "Dice"]

print(tabulate(mydata, headers=headers, tablefmt="grid"))

# Save the summary to a file
filename = input("\nEnter filename to save the summary (e.g., summary.txt): ")

table_output = tabulate(mydata, headers=headers, tablefmt="grid")

with open(filename, "w") as f:
    f.write("GAME SUMMARY\n")
    f.write("="*50 + "\n")
    f.write(table_output + "\n\n")
    f.write(f"Final score: Player 1: {player1_wins}, Player 2: {player2_wins}\n")
    f.write(f"Total rounds played: {len(player1_rolls)}\n")

print(f"\nSummary saved to file: {filename}")