def decimal_to_octal(decimal):
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Input must be a non-negative integer")
    if decimal == 0:
        return "0"
    octal_string = ""
    while decimal > 0:
        remainder = decimal % 8
        octal_string = str(remainder) + octal_string
        decimal //= 8
    return octal_string

if __name__ == '__main__':
    try:
        decimal_input = int(input("Enter a non-negative integer: "))
        octal_output = decimal_to_octal(decimal_input)
        print(f"The octal representation of {decimal_input} is {octal_output}")
    except ValueError as e:
        print(f"Error: {e}")