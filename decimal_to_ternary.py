def decimal_to_ternary(decimal_num: int) -> str:

    if not isinstance(decimal_num, int) or decimal_num < 0:
        raise ValueError("Invalid input. Please provide a non-negative integer.")
    if decimal_num == 0:
        return "0"
    ternary_str = ""
    while decimal_num > 0:
        remainder = decimal_num % 3
        ternary_str = str(remainder) + ternary_str
        decimal_num //= 3
    return ternary_str

if __name__ == '__main__':
    try:
        num_input = int(input("Enter a non-negative integer: "))
        ternary_output = decimal_to_ternary(num_input)
        print(f"The ternary representation of {num_input} is: {ternary_output}")
    except ValueError as e:
        print(f"Error: {e}")