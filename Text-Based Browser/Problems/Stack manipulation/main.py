import collections

my_stack = collections.deque()
n = int(input())
for _ in range(n):
    op = input().split()
    if op[0] == 'POP':
        my_stack.pop()
    else:
        my_stack.append(op[1])
for _ in range(len(my_stack)):
    print(my_stack.pop())
