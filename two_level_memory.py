def two_level_memory_analysis(h1: float, t1: float, t2: float) -> float:
    """Calculates the average memory access time for a two-level memory system."""
    if not (0 <= h1 <= 1):
        raise ValueError("Hit rate (h1) must be between 0 and 1.")
    return h1 * t1 + (1 - h1) * (t1 + t2)

if __name__ == '__main__':
    try:
        h1_in = float(input("Enter hit rate of cache (h1): "))
        t1_in = float(input("Enter access time of cache (t1) in ns: "))
        t2_in = float(input("Enter access time of main memory (t2) in ns: "))
        avg_time = two_level_memory_analysis(h1_in, t1_in, t2_in)
        print(f"Average memory access time: {avg_time:.2f} ns")
    except ValueError as e:
        print(f"Error: {e}")