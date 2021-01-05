x, y = int(input()), int(input())

if x in [1, 8] and y in [1, 8]:
    print(3)
elif x == 1 or x == 8 or y == 8 or y == 1:
    print(5)
else:
    print(8)
