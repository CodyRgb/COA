def to_binary(num: int, bits: int) -> str:
    if num >= 0:
        return format(num, '0' + str(bits) + 'b')
    else:
        return format((1 << bits) + num, '0' + str(bits) + 'b')

def from_binary(binary_str: str) -> int:
    n = len(binary_str)
    if binary_str[0] == '1':
        return int(binary_str, 2) - (1 << n)
    else:
        return int(binary_str, 2)

def bin_add(a: str, b: str) -> str:
    return to_binary(from_binary(a) + from_binary(b), len(a))

def non_restoring_division(dividend: int, divisor: int) -> tuple[int, int]:
    if divisor == 0:
        raise ZeroDivisionError("Division by zero")

    n = max(len(bin(abs(dividend))), len(bin(abs(divisor)))) - 2
    
    quotient = to_binary(dividend, n)
    divisor_binary = to_binary(divisor, n + 1)
    divisor_neg_binary = to_binary(-divisor, n + 1)
    accumulator = '0' * (n + 1)

    for i in range(n):
        if accumulator[0] == '0':
            accumulator = accumulator[1:] + quotient[0]
            accumulator = bin_add(accumulator, divisor_neg_binary)
        else:
            accumulator = accumulator[1:] + quotient[0]
            accumulator = bin_add(accumulator, divisor_binary)

        if accumulator[0] == '0':
            quotient = quotient[1:] + '1'
        else:
            quotient = quotient[1:] + '0'

    if accumulator[0] == '1':
        accumulator = bin_add(accumulator, divisor_binary)

    return from_binary(quotient), from_binary(accumulator)
if __name__ == '__main__':
    try:
        dividend_input = int(input("Enter the dividend (integer): "))
        divisor_input = int(input("Enter the divisor (integer): "))
        quotient_output, remainder_output = non_restoring_division(dividend_input, divisor_input)
        print(f"The quotient is: {quotient_output}")
        print(f"The remainder is: {remainder_output}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Please enter valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please try again.")
        