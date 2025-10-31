def decimal_to_base5(decimal):
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Input must be a non-negative integer")
    if decimal == 0:
        return "0"
    base5_string = ""
    while decimal > 0:
        remainder = decimal % 5
        base5_string = str(remainder) + base5_string
        decimal //= 5
    return base5_string

if __name__ == '__main__':
    try:
        decimal_input = int(input("Enter a non-negative integer: "))
        base5_output = decimal_to_base5(decimal_input)
        print(f"The base-5 representation of {decimal_input} is {base5_output}")
    except ValueError as e:
        print(f"Error: {e}")