# multiplayer-battle-of-dices-dict.py
# multiplayer Battle of Dices using dictionaries

import random

def get_players():
    num_players = int(input("How many players? "))
    players = []
    for i in range(num_players):
        player = {
            "name": input(f"Enter name of player {i+1}: "),
            "email": input("Enter email: "),
            "country": input("Enter country: "),
            "score": 0,     # total rounds won
            "rolls": []     # all dice rolls (for auditing)
        }
        players.append(player)
        print()
    return players

def play_round(players):
    print("Rolling the dice...")
    highest_roll = 0
    round_winners = []

    for p in players:
        roll = random.randint(1, 6)
        p["rolls"].append(roll)
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

def check_winner(players, target=3):
    for p in players:
        if p["score"] >= target:
            return p
    return None

def show_final_results(players, winner):
    print("\n===== Final Results =====")
    print(f"Winner: {winner['name']} ({winner['country']}) — Score: {winner['score']}")
    print("\nAll players:")
    for p in players:
        print(f"- {p['name']} | {p['email']} | {p['country']} | Score: {p['score']} | Rolls: {p['rolls']}")

def maybe_save_to_file(players, winner):
    choice = input("\nDo you want to save the results to a file? (y/n): ").strip().lower()
    if choice != "y":
        return
    filename = input("Enter filename (default: results_multiplayer_dict.txt): ").strip() or "results_multiplayer_dict.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("===== Final Results =====\n")
            f.write(f"Winner: {winner['name']} ({winner['country']}) — Score: {winner['score']}\n\n")
            f.write("All players:\n")
            for p in players:
                f.write(f"- {p['name']} | {p['email']} | {p['country']} | Score: {p['score']} | Rolls: {p['rolls']}\n")
        print(f"Results saved to '{filename}'.")
    except Exception as e:
        print(f"Could not save file: {e}")

def main():
    print("=== Multiplayer Battle of Dices (Dict Version) ===\n")
    players = get_players()

    print("--- Let the dice battle begin! ---\n")
    winner = None
    while not winner:
        play_round(players)
        winner = check_winner(players, target=3)

    print(f" {winner['name']} from {winner['country']} wins the game! ")
    show_final_results(players, winner)
    maybe_save_to_file(players, winner)

if __name__ == "__main__":
    main()