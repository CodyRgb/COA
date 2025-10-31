import struct

def float_to_ieee754(num):
    print(f"Enter the Decimal Number = {num}")

    int_part = int(abs(num))
    frac_part = abs(num) - int_part
    int_bin = bin(int_part).replace("0b", "")
    frac_bin = ""
    while frac_part and len(frac_bin) < 10:
        frac_part *= 2
        if frac_part >= 1:
            frac_bin += "1"
            frac_part -= 1
        else:
            frac_bin += "0"
    print(f"Given number in Binary = {int_bin}.{frac_bin}")

    shift = len(int_bin) - 1
    mantissa = int_bin[1:] + frac_bin
    print(f"Given number in Scientific Notation = 1.{mantissa} * 2^{shift}")
    print(f"Real Exponent = {shift}")

    biased_exp = shift + 127
    exp_bin = format(biased_exp, "08b")
    print("Select the destination floating point format = 32 bit")
    print(f"Biased Exponent = {shift} + 127 = {biased_exp} = {exp_bin}")

    mantissa_23 = (mantissa + "0" * 23)[:23]
    print(f"Actual fractional part = {mantissa}")
    print(f"Mantissa of 23 bits = {mantissa_23}")

    sign_bit = "0" if num >= 0 else "1"
    print(f"Sign bit = {sign_bit}")

    ieee_32bit = sign_bit + exp_bin + mantissa_23
    print(f"32 bit representation of the given number = {ieee_32bit}")

    packed = struct.pack('!f', num)
    hex_str = hex(int.from_bytes(packed, 'big')).upper().replace("0X", "")
    print(f"Hex representation = {hex_str}")


if __name__ == '__main__':
    num = float(input("Enter a decimal number: "))
    float_to_ieee754(num)
    