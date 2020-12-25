length = int(input())
for i in range(0, length):
    print(("#" * (i * 2 + 1)).center(length * 2 - 1))
