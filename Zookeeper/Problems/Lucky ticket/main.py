# Save the input in this variable
ticket = input()

# Add up the digits for each half
l = list(ticket)
half1 = int(l[0]) + int(l[1]) + int(l[2])
half2 = int(l[3]) + int(l[4]) + int(l[5])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")