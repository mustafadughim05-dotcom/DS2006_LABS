import random

# 1) Number of players
num_players = int(input("Enter the number of players: "))

# 2) Players' names
players = []
for i in range(num_players):
    name = input(f"Enter the name for player {i+1}: ")
    players.append(name)

# 3) Scores (all start at 0)
scores = [0] * num_players

# Target wins (keep simple like in lecture)
TARGET_WINS = 3

# 4) Game loop
while max(scores) < TARGET_WINS:
    print("\n--- New Round ---")

    # 5) Rolls for this round (one total per player)
    # (If needed later, this could be a nested list for per-die details)
    rolls = [0] * num_players

    # Example dice from the slides (d8 + d12). Keep it simple and consistent.
    for i in range(num_players):
        d8 = random.randint(1, 8)
        d12 = random.randint(1, 12)
        total = d8 + d12
        rolls[i] = total
        print(f"{players[i]} rolled {d8} + {d12} = {total}")

    # 6) Determine round winner(s)
    max_roll = max(rolls)
    winners_idx = [i for i, r in enumerate(rolls) if r == max_roll]

    if len(winners_idx) == 1:
        w = winners_idx[0]
        scores[w] += 1
        print(f"Round winner: {players[w]}")
    else:
        print("It's a tie! No points awarded.")

    # 7) Show current scores
    for i in range(num_players):
        print(f"{players[i]}: {scores[i]} wins")

# 8) End of game: announce champion(s)
print("\n=== Game Over! ===")
best = max(scores)
champions = [players[i] for i, s in enumerate(scores) if s == best]

if len(champions) == 1:
    print(f"The champion is {champions[0]} with {best} wins!")
else:
    print("We have multiple champions: " + ", ".join(champions))