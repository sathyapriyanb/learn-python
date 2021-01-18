# read sample.txt and print the number of lines
f = open('sample.txt')
print(len(f.readlines()))
f.close()