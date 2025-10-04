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

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Battle of Dices - BAD VERSION 
# This version runs without any loops - just copying code multiple times
# Round 1
print("\n=== ROUND 1 ===")
input("Press ENTER to roll the dice...")

player1_roll = random.randint(1, 20)
player2_roll = random.randint(1, 20)

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

input("Press ENTER to continue...")

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

# Round 2
print("\n=== ROUND 2 ===")
input("Press ENTER to roll the dice...")

player1_roll = random.randint(1, 20)
player2_roll = random.randint(1, 20)

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

input("Press ENTER to continue...")

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

# Round 3
print("\n=== ROUND 3 ===")
input("Press ENTER to roll the dice...")

player1_roll = random.randint(1, 20)
player2_roll = random.randint(1, 20)

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

input("Press ENTER to continue...")

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

# Round 4
print("\n=== ROUND 4 ===")
input("Press ENTER to roll the dice...")

player1_roll = random.randint(1, 20)
player2_roll = random.randint(1, 20)

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

input("Press ENTER to continue...")

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

# Round 5
print("\n=== ROUND 5 ===")
input("Press ENTER to roll the dice...")

player1_roll = random.randint(1, 20)
player2_roll = random.randint(1, 20)

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

input("Press ENTER to continue...")

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

# Round 6 (in case of many ties)
print("\n=== ROUND 6 ===")
input("Press ENTER to roll the dice...")

player1_roll = random.randint(1, 20)
player2_roll = random.randint(1, 20)

print("Player 1 rolled: ", player1_roll)
print("Player 2 rolled: ", player2_roll)

input("Press ENTER to continue...")

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win? ")

print("\nGame over! (Maximum 6 rounds played)")