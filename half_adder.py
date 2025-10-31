def half_adder(a, b):
    sum_result = a ^ b
    carry_out = a & b
    return (sum_result, carry_out)

if __name__ == '__main__':
    x = int(input("Enter first binary digit (0 or 1): "))
    y = int(input("Enter second binary digit (0 or 1): "))
    sum_output, carry_output = half_adder(x, y)
    print(f"The sum is: {sum_output}")
    print(f"The carry is: {carry_output}")
