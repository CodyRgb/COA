def decimal_to_hexadecimal(decimal_num: int) -> str:
    if not isinstance(decimal_num, int) or decimal_num < 0:
        raise ValueError("Invalid input. Please provide a non-negative integer.")
    if decimal_num == 0:
        return "0"
    hexadecimal_str = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        if remainder < 10:
            hexadecimal_str = str(remainder) + hexadecimal_str
        else:
            hexadecimal_str = chr(ord('A') + remainder - 10) + hexadecimal_str
        decimal_num //= 16
    return hexadecimal_str

if __name__ == '__main__':
    try:
        num_input = int(input("Enter a non-negative integer: "))
        hex_output = decimal_to_hexadecimal(num_input)
        print(f"The hexadecimal representation of {num_input} is: {hex_output}")
    except ValueError as e:
        print(f"Error: {e}")