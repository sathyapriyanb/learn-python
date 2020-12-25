# put your python code here
seq = input().split()
c = input()
temp = " ".join([str(i) for i in range(len(seq)) if seq[i] == c])
print(temp if temp else "not found")
