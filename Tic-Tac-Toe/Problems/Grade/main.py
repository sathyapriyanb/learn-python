score, max_score = abs(int(input())), abs(int(input()))
score_percent = score * 100/max_score

if score_percent >= 90:
    print("A")
elif score_percent >= 80:
    print("B")
elif score_percent >= 70:
    print("C")
elif score_percent >= 60:
    print("D")
else:
    print("F")
