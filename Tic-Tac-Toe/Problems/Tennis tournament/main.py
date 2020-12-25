win = [game.replace(" win", "")for game in [input() for _ in range(int(input()))] if game.endswith("win")]
print(win)
print(len(win))
