size = int(input())
print('\n'.join([('#' * (i * 2 + 1)).center(size * 2 - 1) for i in range(0, size)]))