s = input()
new_s = s[0].lower()

for c in s[1:]:
    new_s += "_" + c.lower() if c.isupper() else c
print(new_s)
