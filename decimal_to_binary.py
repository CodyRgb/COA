def decimal_to_binary(decimal):
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Input must be a non-negative integer")
    if decimal == 0:
        return "0"
    binary_string = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_string = str(remainder) + binary_string
        decimal //= 2
    return binary_string

if __name__ == '__main__':
    try:
        decimal_input = int(input("Enter a non-negative integer: "))
        binary_output = decimal_to_binary(decimal_input)
        print(f"The binary representation of {decimal_input} is {binary_output}")
    except ValueError as e:
        print(f"Error: {e}")
