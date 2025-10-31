def to_twos_complement(num: int, bits: int) -> str:
    if num >= 0:
        return format(num, '0' + str(bits) + 'b')
    else:
        return format((1 << bits) + num, '0' + str(bits) + 'b')


def from_twos_complement(binary_str: str) -> int:
    n = len(binary_str)
    if binary_str[0] == '1':
        return int(binary_str, 2) - (1 << n)
    else:
        return int(binary_str, 2)


def bin_add(a: str, b: str) -> str:
    return to_twos_complement(from_twos_complement(a) + from_twos_complement(b), len(a))


def arithmetic_right_shift(binary_str: str) -> str:
    return binary_str[0] + binary_str[:-1]


def booths_multiplication(multiplicand: int, multiplier: int) -> tuple:
    n = max(len(bin(abs(multiplicand))), len(bin(abs(multiplier)))) - 1
    m = to_twos_complement(multiplicand, n + 1)
    q = to_twos_complement(multiplier, n)
    acc = '0' * (n + 1)
    q_minus_1 = '0'
    multiplicand_binary = to_twos_complement(multiplicand, n + 1)
    multiplier_binary = to_twos_complement(multiplier, n)

    for _ in range(n):
        if q[-1] == '1' and q_minus_1 == '0':
            acc = bin_add(acc, to_twos_complement(-from_twos_complement(m), n + 1))
        elif q[-1] == '0' and q_minus_1 == '1':
            acc = bin_add(acc, m)
        
        shifted = arithmetic_right_shift(acc + q + q_minus_1)
        acc, q, q_minus_1 = shifted[:n+1], shifted[n+1:2*n+1], shifted[2*n+1:]

    product = from_twos_complement(acc + q)
    product_binary = acc + q
    
    return product, multiplicand_binary, multiplier_binary, product_binary


if __name__ == '__main__':
    try:
        multiplicand_input = int(input("Enter the multiplicand: "))
        multiplier_input = int(input("Enter the multiplier: "))
        product, m_bin, q_bin, p_bin = booths_multiplication(multiplicand_input, multiplier_input)
        print(f"Multiplicand ({multiplicand_input}) in binary: {m_bin}")
        print(f"Multiplier ({multiplier_input}) in binary: {q_bin}")
        print(f"Product in decimal: {product}")
        print(f"Product in binary: {p_bin}")
    except ValueError:
        print("Invalid input. Please enter integers.")
