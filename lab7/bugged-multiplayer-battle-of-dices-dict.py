# bugged-multiplayer-battle-of-dices-dict.py
# This version is intentionally bugged because it uses a shallow copy.

import random

# Template for a player – notice that 'rolls' is a LIST (nested structure)
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "score": 0,
    "rolls": []   # nested structure, will cause the bug
}

number_of_players = int(input("How many players? "))
players = []

# --------- Here is the intentional BUG ----------
# Instead of deepcopy, we only use a shallow copy
for i in range(number_of_players):
    player = player_info.copy()  # <-- shallow copy (bug!)
    player["name"] = input(f"What is the name of Player {i+1}? ")
    player["email"] = input(f"What is the e-mail of Player {i+1}? ")
    player["country"] = input(f"What is the country of Player {i+1}? ")
    players.append(player)
# -----------------------------------------------

print("\n--- Let the dice battle begin! ---\n")

winner = None
while not winner:
    highest_roll = 0
    round_winners = []
    for p in players:
        roll = random.randint(1, 6)
        p["rolls"].append(roll)  # all players share the SAME list here
        print(f"{p['name']} rolled {roll}")
        if roll > highest_roll:
            highest_roll = roll
            round_winners = [p]
        elif roll == highest_roll:
            round_winners.append(p)

    if len(round_winners) == 1:
        round_winners[0]["score"] += 1
        print(f"--> {round_winners[0]['name']} wins this round!\n")
    else:
        print("--> It's a tie this round!\n")

    # check if someone reached 2 points (to finish faster)
    for p in players:
        if p["score"] >= 2:
            winner = p
            break

print("\nFinal results:")
for p in players:
    print(f"- {p['name']} | {p['country']} | score={p['score']} | rolls={p['rolls']}")