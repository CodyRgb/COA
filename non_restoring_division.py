M = int(input("Enter the Divisor (M) = "))
Q = int(input("Enter the Dividend (Q) = "))
n = max(M, Q).bit_length()
A = 0
mask = (1 << n) - 1
print("Binary representation of Dividend (Q) =", format(Q, f'0{n}b'))
print("Binary representation of Divisor (M) =", format(M, f'0{n}b'))

for _ in range(n):
    if A >= 0:
        A = (A << 1) | ((Q >> (n - 1)) & 1)
        Q = (Q << 1) & mask
        A = A - M
    else:
        A = (A << 1) | ((Q >> (n - 1)) & 1)
        Q = (Q << 1) & mask
        A = A + M
    
    if A >= 0:
        Q |= 1
    else:
        Q &= mask - 1

if A < 0:
    A = A + M

print("Quotient in binary =", format(Q, f'0{n}b'))
print("Remainder in binary =", format(A, f'0{n}b'))
