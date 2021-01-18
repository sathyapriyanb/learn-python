# read test.txt
f = open('test.txt')
for data in f:
    print(data[0])
f.close()