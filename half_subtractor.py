def half_subtractor(a, b):
    difference = a ^ b
    borrow = (~a) & b
    return (difference, borrow)

if __name__ == '__main__':
    x = int(input("Enter first bit (0 or 1): "))
    y = int(input("Enter second bit (0 or 1): "))
    difference_output, borrow_output = half_subtractor(x, y)
    print(f"The difference is: {difference_output}")
    print(f"The borrow is: {borrow_output}")
