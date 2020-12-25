s = input()
new_s = ""

for c in s:
    new_s += "_" + c.lower() if c.isupper() else c
print(new_s)