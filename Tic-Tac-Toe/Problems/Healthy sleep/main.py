a = abs(int(input()))
b = abs(int(input()))
h = abs(int(input()))

print("Normal" if(a <= h <= b) else "Excess" if (b < h) else "Deficiency")
