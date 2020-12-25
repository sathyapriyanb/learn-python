atoms = abs(int(input()))
final_quantity = abs(int(input()))

i = 0
while atoms > final_quantity:
    # print(atoms)
    atoms /= 2
    i += 1

print(i * 12)