# put your python code here
import math

a, b, c = [int(input()) for i in range(3)]
p = math.fsum([a, b, c]) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)