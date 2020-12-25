# put your python code here
inpt = int(input())
print("Leap" if (inpt % 4 == 0) and (inpt % 100 != 0 or inpt % 400 == 0) else "Ordinary")