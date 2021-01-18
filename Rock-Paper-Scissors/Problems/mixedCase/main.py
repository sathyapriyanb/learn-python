words = input().lower().split()
for i in range(1, len(words)):
    words[i] = words[i].title()
print("".join(words))