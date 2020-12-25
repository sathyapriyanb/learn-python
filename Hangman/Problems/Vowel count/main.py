string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0
for c in vowels:
    count += string.count(c)
print(count)