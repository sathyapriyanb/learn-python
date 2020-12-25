n = int(input())
nums = [int(input()) for _ in range(n)]
for num in nums:
    if num % 7 == 0:
        print(num ** 2)