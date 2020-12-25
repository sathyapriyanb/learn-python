amount = abs(int(input()))
counter = 0
while amount < 700000:
    amount += amount * 7.1 / 100
    counter += 1
print(counter)