s = input().lower()
for a in s:
    if a in "aeiou":
        print("vowel")
    elif a.isalpha():
        print("consonant")
    else:
        break