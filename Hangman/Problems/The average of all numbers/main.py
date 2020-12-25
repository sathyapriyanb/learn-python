# put your python code here
a, b = int(input()), int(input())
num = [i for i in range(a, b+1) if i % 3 == 0]
mean = sum(num) / len(num)
print(mean)
