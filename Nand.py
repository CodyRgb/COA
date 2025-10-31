def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return a ^ b

print("NAND Gate:")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} NAND {b} = {int(NAND(a, b))}")

print("\nNOR Gate:")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} NOR {b} = {int(NOR(a, b))}")

print("\nXOR Gate:")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} XOR {b} = {XOR(a, b)}")

