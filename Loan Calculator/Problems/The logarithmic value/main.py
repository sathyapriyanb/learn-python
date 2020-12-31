import math

x, b = [int(input()) for i in range(2)]
if b <= 0 or b == 1:
    print(round(math.log(x), 2))
else:
    print(round(math.log(x, b), 2))
