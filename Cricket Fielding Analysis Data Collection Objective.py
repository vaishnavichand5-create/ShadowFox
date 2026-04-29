data = [
    [1, 1, "MI", "Player A", 2, "Cover", "Quick stop", "Clean Pick", "-", 1, 3, "Mumbai"],
    [1, 1, "MI", "Player B", 4, "Mid-off", "Direct hit run out", "Good Throw", "Run Out", 2, 5, "Mumbai"],
    [1, 1, "MI", "Player C", 6, "Deep", "Dropped catch", "Drop Catch", "-", -4, 7, "Mumbai"],
]

players = {}

for row in data:
    player = row[3]
    pick = row[7]
    throw = row[8]
    runs = row[9]

    if player not in players:
        players[player] = {
            "Total Chances": 0,
            "Clean Picks": 0,
            "Catches": 0,
            "Drops": 0,
            "Run Outs": 0,
            "Missed Chances": 0,
            "Runs Saved": 0,
            "Runs Conceded": 0
        }

    players[player]["Total Chances"] += 1

    if pick == "Clean Pick":
        players[player]["Clean Picks"] += 1
    elif pick == "Catch":
        players[player]["Catches"] += 1
    elif pick == "Drop Catch":
        players[player]["Drops"] += 1
        players[player]["Missed Chances"] += 1

    if throw == "Run Out":
        players[player]["Run Outs"] += 1

    if runs > 0:
        players[player]["Runs Saved"] += runs
    else:
        players[player]["Runs Conceded"] += abs(runs)

print("\nFielding Performance Matrix\n")

for player, stats in players.items():
    print(f"Player: {player}")
    for key, value in stats.items():
        print(f"{key}: {value}")
    print("-" * 30)