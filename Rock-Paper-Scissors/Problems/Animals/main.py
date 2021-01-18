# read animals.txt
# and write animals_new.txt
f1 = open('animals.txt')
f2 = open('animals_new.txt', 'w')
data = f1.readlines()
data = [line.replace('\n', ' ') for line in data]
f2.writelines(data)
f1.close()
f2.close()

