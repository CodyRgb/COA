def to_binary(num, bits):
    binary = bin(num)[2:]
    binary = binary.zfill(bits)
    if len(binary) > bits:
        binary = binary[-bits:]
    return binary

divisor = int(input("Enter the Divisor (M): "))
dividend = int(input("Enter the Dividend (Q): "))

n = max(len(bin(abs(dividend))[2:]), len(bin(abs(divisor))[2:]))

bin_divisor = to_binary(divisor, n)
bin_dividend = to_binary(dividend, n)

print("Binary representation of Dividend (Q) :", bin_dividend)
print("Binary representation of Divisor (M):", bin_divisor)

A = 0
Q = dividend
M = divisor
count = n

while count > 0:
    A = (A << 1) | ((Q >> (n - 1)) & 1)
    Q = (Q << 1) & ((1 << n) - 1)
    
    A = A - M
    
    if A < 0:
        A = A + M
        Q = Q & ~1
    else:
        Q = Q | 1
    
    count -= 1

print("Quotient in binary:", to_binary(Q, n))
print("Remainder in binary:", to_binary(A, n))