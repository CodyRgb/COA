c1 = float(input("C1 (cost/bit of Level 1) = "))
c2 = float(input("C2 (cost/bit of Level 2) = "))
c3 = float(input("C3 (cost/bit of Level 3) = "))
s1 = int(input("S1 (size of Level 1 in bits) = "))
s2 = int(input("S2 (size of Level 2 in bits) = "))
s3 = int(input("S3 (size of Level 3 in bits) = "))
h1 = float(input("Hit ratio (h1) for Level 1 = "))
h2 = float(input("Hit ratio (h2) for Level 2 = "))
t1 = float(input("Access time of Level 1 (t1, in microseconds) = "))
t2 = float(input("Access time of Level 2 (t2, in microseconds) = "))
t3 = float(input("Access time of Level 3 (t3, in microseconds) = "))

total_cost = c1 * s1 + c2 * s2 + c3 * s3
total_size = s1 + s2 + s3
avg_cost_per_bit = total_cost / total_size
avg_access_time = h1 * t1 + (1 - h1) * h2 * t2 + (1 - h1) * (1 - h2) * t3

print(f"\nAverage Cost per Bit: {avg_cost_per_bit:.6f} INR")
print(f"Average Access Time: {avg_access_time:.6f} microseconds")
