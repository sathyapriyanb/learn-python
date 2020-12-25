count = int(input())
if count < 1:
    print("no army")
elif count < 10:
    print("few")
elif count < 50:
    print("pack")
elif count < 500:
    print("horde")
elif count < 1000:
    print("swarm")
else:
    print("legion")