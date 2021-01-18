# read sums.txt
f = open('sums.txt')
for line in f:
    num = line.split(" ")
    print(int(num[0]) + int(num[1]))
f.close()

