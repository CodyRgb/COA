def three_level_memory_analysis(h1: float, h2: float, t1: float, t2: float, t3: float) -> float:
    """Calculates the average memory access time for a three-level memory system."""
    if not (0 <= h1 <= 1 and 0 <= h2 <= 1):
        raise ValueError("Hit rates (h1, h2) must be between 0 and 1.")
    return h1 * t1 + (1 - h1) * h2 * t2 + (1 - h1) * (1 - h2) * t3

if __name__ == '__main__':
    try:
        h1_in = float(input("Enter hit rate of L1 cache (h1): "))
        h2_in = float(input("Enter hit rate of L2 cache (h2): "))
        t1_in = float(input("Enter access time of L1 cache (t1) in ns: "))
        t2_in = float(input("Enter access time of L2 cache (t2) in ns: "))
        t3_in = float(input("Enter access time of main memory (t3) in ns: "))
        avg_time = three_level_memory_analysis(h1_in, h2_in, t1_in, t2_in, t3_in)
        print(f"Average memory access time: {avg_time:.2f} ns")
    except ValueError as e:
        print(f"Error: {e}")