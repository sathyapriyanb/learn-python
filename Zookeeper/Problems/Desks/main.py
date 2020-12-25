# put your python code here
a = abs(int(input()))
b = abs(int(input()))
c = abs(int(input()))
if a % 2:
    a += 1
if b % 2:
    b += 1
if c % 2:
    c += 1
a //= 2
b //= 2
c //= 2
print(a + b + c)
