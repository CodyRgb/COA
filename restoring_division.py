def to_binary(num: int, bits: int) -> str:
    """Converts an integer to a two's complement binary string."""
    if num >= 0:
        return format(num, '0' + str(bits) + 'b')
    else:
        return format((1 << bits) + num, '0' + str(bits) + 'b')

def from_binary(binary_str: str) -> int:
    """Converts a two's complement binary string to an integer."""
    if binary_str[0] == '1':
        return int(binary_str, 2) - (1 << len(binary_str))
    else:
        return int(binary_str, 2)

def bin_add(a: str, b: str) -> str:
    """Adds two two's complement binary strings."""
    return to_binary(from_binary(a) + from_binary(b), len(a))

def restoring_division(dividend: int, divisor: int) -> tuple[int, int]:
    """Performs restoring division of two integers."""
    if divisor == 0:
        raise ZeroDivisionError("Division by zero")

    n = max(len(bin(abs(dividend))), len(bin(abs(divisor)))) - 2
    quotient = to_binary(dividend, n)
    divisor_binary = to_binary(divisor, n + 1)
    accumulator = '0' * (n + 1)
    divisor_neg = to_binary(-divisor, n + 1)

    for _ in range(n):
        accumulator = accumulator[1:] + quotient[0]
        accumulator = bin_add(accumulator, divisor_neg)
        if accumulator[0] == '1':
            quotient = quotient[1:] + '0'
            accumulator = bin_add(accumulator, divisor_binary)
        else:
            quotient = quotient[1:] + '1'

    return from_binary(quotient), from_binary(accumulator)

if __name__ == '__main__':
    try:
        dividend_input = int(input("Enter the dividend: "))
        divisor_input = int(input("Enter the divisor: "))
        q, r = restoring_division(dividend_input, divisor_input)
        print(f"Quotient: {q}, Remainder: {r}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")