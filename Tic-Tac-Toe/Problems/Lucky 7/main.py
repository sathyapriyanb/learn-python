n = int(input())
input_list = [int(input()) for _ in range(n)]
for i in input_list:
    if not i % 7:
        print(i ** 2)
