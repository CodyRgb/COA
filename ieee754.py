import struct

def float_to_ieee754(float_num: float) -> str:
    """Converts a float to its 32-bit IEEE 754 binary representation."""
    packed = struct.pack('!f', float_num)
    unpacked = struct.unpack('!I', packed)[0]
    return bin(unpacked)[2:].zfill(32)

def ieee754_to_float(binary_str: str) -> float:
    """Converts a 32-bit IEEE 754 binary string to a float."""
    if len(binary_str) != 32:
        raise ValueError("Input binary string must be 32 characters long.")
    unpacked = int(binary_str, 2)
    packed = struct.pack('!I', unpacked)
    return struct.unpack('!f', packed)[0]

if __name__ == '__main__':
    try:
        choice = input("Choose conversion: (1) float to IEEE 754, (2) IEEE 754 to float: ")
        if choice == '1':
            num = float(input("Enter a float: "))
            print(f"IEEE 754 representation: {float_to_ieee754(num)}")
        elif choice == '2':
            binary = input("Enter a 32-bit binary string: ")
            print(f"Float value: {ieee754_to_float(binary)}")
        else:
            print("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}")