inp = [int(i) for i in input()]
print([(inp[i] + inp[i + 1]) / 2 for i in range(len(inp) - 1)])
