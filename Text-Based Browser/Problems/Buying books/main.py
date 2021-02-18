import collections

my_stack = collections.deque()
n = int(input())
for _ in range(n):
    op = input()
    if op[:4] == 'READ':
        print(my_stack.pop())
    else:
        my_stack.append(op[4:])
