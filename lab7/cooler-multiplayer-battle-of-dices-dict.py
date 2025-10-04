# cooler-multiplayer-battle-of-dices-dict.py
# DS2006 – Task 16
# Cooler multiplayer version using dictionaries:
# - configure target score (first to N)
# - configure dice sides (e.g., D6, D20)
# - tie-breaker: automatic re-roll among top rollers
# - keep a full round log
# - final leaderboard
# - optional save to file

import random
from datetime import datetime

# ------------------------- helpers -------------------------

def ask_int(prompt, minimum=None, maximum=None):
    """Ask for an integer with basic validation."""
    while True:
        try:
            x = int(input(prompt).strip())
            if minimum is not None and x < minimum:
                print(f"Please enter a number >= {minimum}.")
                continue
            if maximum is not None and x > maximum:
                print(f"Please enter a number <= {maximum}.")
                continue
            return x
        except ValueError:
            print("Please enter a valid integer.")

def ask_yes_no(prompt):
    """Return True for 'y', False for 'n'."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")

# ------------------------- setup -------------------------

def get_players():
    num_players = ask_int("How many players? ", minimum=2)
    players = []
    for i in range(num_players):
        player = {
            "name": input(f"Enter name of player {i+1}: ").strip() or f"Player{i+1}",
            "email": input("Enter email: ").strip(),
            "country": input("Enter country: ").strip(),
            "score": 0,
            "rolls": []  # all dice rolls across the whole game (audit trail)
        }
        print()
        players.append(player)
    return players

def configure_game():
    print("\n--- Game configuration ---")
    target_score = ask_int("Target score to win (default 3): ", minimum=1)
    dice_sides   = ask_int("How many sides on the die (e.g., 6 for D6, 20 for D20)? ", minimum=2)
    return target_score, dice_sides

# ------------------------- core mechanics -------------------------

def roll_die(sides):
    return random.randint(1, sides)

def play_round(players, sides):
    """
    One round:
      - everyone rolls once
      - if unique highest roll -> that player wins the round (returns [winner])
      - if tie -> tie-breaker: re-roll among tied players until there is exactly one winner
    Returns: (winners_list, round_snapshot)
    """
    # initial rolls
    current = []
    highest = 0
    top = []

    for p in players:
        r = roll_die(sides)
        p["rolls"].append(r)
        current.append({"name": p["name"], "roll": r})
        if r > highest:
            highest = r
            top = [p]
        elif r == highest:
            top.append(p)

    # tie-breaker loop among 'top' until single winner
    tiebreak_logs = []
    while len(top) > 1:
        tb_current = []
        tb_high = 0
        tb_top = []
        for p in top:
            r = roll_die(sides)
            p["rolls"].append(r)
            tb_current.append({"name": p["name"], "roll": r})
            if r > tb_high:
                tb_high = r
                tb_top = [p]
            elif r == tb_high:
                tb_top.append(p)
        tiebreak_logs.append(tb_current)
        top = tb_top

    # now 'top' has exactly one winner
    winner = top[0]
    winner["score"] += 1

    round_snapshot = {
        "initial_rolls": current,
        "tiebreakers": tiebreak_logs,  # list of lists (each list is one tie-breaker roll set)
        "winner": winner["name"]
    }
    return [winner], round_snapshot

def someone_won(players, target):
    for p in players:
        if p["score"] >= target:
            return p
    return None

# ------------------------- output & save -------------------------

def leaderboard(players):
    print("\n===== Leaderboard =====")
    for p in sorted(players, key=lambda x: x["score"], reverse=True):
        print(f"- {p['name']} ({p['country']}) | Score: {p['score']} | Rolls: {p['rolls']}")

def maybe_save(players, rounds, winner, target, sides):
    if not ask_yes_no("\nSave results to file? (y/n): "):
        return
    filename = input("Filename (default: results_cooler_multiplayer_dict.txt): ").strip() or "results_cooler_multiplayer_dict.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=== Multiplayer Battle of Dices (Cooler Dict Version) ===\n")
            f.write(f"Timestamp: {datetime.now().isoformat(timespec='seconds')}\n")
            f.write(f"Die sides: D{sides}\n")
            f.write(f"Target score: {target}\n\n")
            f.write(f"Winner: {winner['name']} ({winner['country']}) — Score: {winner['score']}\n\n")
            f.write("Players:\n")
            for p in players:
                line = f"- {p['name']} | {p['email']} | {p['country']} | Score: {p['score']} | Rolls: {p['rolls']}\n"
                f.write(line)
            f.write("\nRound log:\n")
            for i, r in enumerate(rounds, start=1):
                f.write(f"Round {i}: initial={[(x['name'], x['roll']) for x in r['initial_rolls']]}, ")
                if r["tiebreakers"]:
                    tb_str = "; ".join(str([(x['name'], x['roll']) for x in t]) for t in r["tiebreakers"])
                    f.write(f"tiebreakers={tb_str}, ")
                f.write(f"winner={r['winner']}\n")
        print(f"Results saved to '{filename}'.")
    except Exception as e:
        print(f"Could not save file: {e}")

# ------------------------- main ------------------------
def main():
    print("=== Multiplayer Battle of Dices (Cooler Dict Version) ===")
    players = get_players()
    target_score, dice_sides = configure_game()

    print("\n--- Let the dice battle begin! ---\n")
    rounds_log = []
    winner = None

    while not winner:
        winners, snap = play_round(players, dice_sides)
        print(f"--> {winners[0]['name']} wins this round!\n")
        rounds_log.append(snap)
        winner = someone_won(players, target_score)

    print(f" {winner['name']} from {winner['country']} wins the game! (Target = {target_score}, Die = D{dice_sides}) ")
    leaderboard(players)
    maybe_save(players, rounds_log, winner, target_score, dice_sides)

if __name__ == "__main__":
    main()