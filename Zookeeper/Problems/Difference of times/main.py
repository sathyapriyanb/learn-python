# put your python code here
h1 = abs(int(input()))
m1 = abs(int(input()))
s1 = abs(int(input()))

h2 = abs(int(input()))
m2 = abs(int(input()))
s2 = abs(int(input()))

h = h2 - h1
m = m2 - m1
s = s2 - s1

print(h * 60 * 60 + m * 60 + s)
