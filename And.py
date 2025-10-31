def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return 1 - a

print("AND Gate:")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} AND {b} = {AND(a, b)}")

print("\nOR Gate:")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} OR {b} = {OR(a, b)}")

print("\nNOT Gate:")
for a in [0, 1]:
    print(f"NOT {a} = {NOT(a)}")
