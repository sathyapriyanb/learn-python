# Save the input in this variable
ticket = input()
lst = [int(i) for i in list(ticket)]
# Add up the digits for each half
half1 = sum(lst[0:3])
half2 = sum(lst[-1:-4:-1])
# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")