# put your python code here
lower_limit = int(input())
upper_limit = int(input())
total = 0
counter = 0
for i in range(lower_limit, upper_limit+1):
    if not i % 3:
        total += i
        counter += 1
print(total / counter)