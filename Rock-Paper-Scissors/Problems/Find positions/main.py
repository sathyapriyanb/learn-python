numbers, find = input().split(), input()
print(*([i for i in range(0, len(numbers)) if numbers[i] == find]) if find in numbers else ["not found"])
