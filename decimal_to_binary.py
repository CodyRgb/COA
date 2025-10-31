def convert_int(int_part, base):
    if base == 1:
        return '1' * int_part
    elif int_part == 0:
        return '0'
    result = ''
    while int_part > 0:
        result = str(int_part % base) + result
        int_part //= base
    return result

def convert_frac(frac_part, base, precision=6):
    result = ''
    count = 0
    while frac_part > 0 and count < precision:
        frac_part *= base
        digit = int(frac_part)
        result += str(digit)
        frac_part -= digit
        count += 1
    return result if result else '0'

decimal_input = float(input("Enter the decimal number: "))
base = 2
int_part = int(decimal_input)
frac_part = decimal_input - int_part
converted_int = convert_int(int_part, base)
converted_frac = convert_frac(frac_part, base)
print(f"Decimal {int_part} converted into Base-{base} system = {converted_int}")
print(f"Fractional decimal {round(frac_part, 6)} converted into Base-{base} system = 0.{converted_frac}")
print(f"Hence, Base-{base} equivalent of input decimal = {converted_int}.{converted_frac}")