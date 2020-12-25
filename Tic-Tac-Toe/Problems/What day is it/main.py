ref_day = "Tuesday"
prev_day = "Monday"
next_day = "Wednesday"

ref_time = "10:30"

offset = int(input())
actual_time = int(ref_time[:2]) + offset

if actual_time >= 24:
    print(next_day)
elif actual_time < 0:
    print(prev_day)
else:
    print(ref_day)