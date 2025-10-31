def three_level_memory_analysis():
    c1 = float(input("C1 = "))
    c2 = float(input("C2 = "))
    c3 = float(input("C3 = "))
    s1 = int(input("S1 = "))
    s2 = int(input("S2 = "))
    s3 = int(input("S3 = "))
    h1 = float(input("H1 = "))
    h2 = float(input("H2 = "))
    h3 = float(input("H3 = "))
    t1 = float(input("ta1 = "))
    t2 = float(input("ta2 = "))
    t3 = float(input("ta3 = "))
    
    total_cost = c1 * s1 + c2 * s2 + c3 * s3
    total_size = s1 + s2 + s3
    avg_cost_per_bit = total_cost / total_size
    avg_access_time = h1 * t1 + (1 - h1) * h2 * t2 + (1 - h1) * (1 - h2) * h3 * t3
    
    print(f"Average Cost per Bit: {avg_cost_per_bit:.6f} INR")
    print(f"Average Access Time: {avg_access_time:.6f} microseconds")


if __name__ == '__main__':
    three_level_memory_analysis()
