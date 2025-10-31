c1 = float(input("C1 (cost/bit of Level 1) = "))
c2 = float(input("C2 (cost/bit of Level 2) = "))
s1 = int(input("S1 (size of Level 1 in bits) = "))
s2 = int(input("S2 (size of Level 2 in bits) = "))
h = float(input("Hit ratio (h) = "))
t1 = float(input("Access time of Level 1 (t1, in microseconds) = "))
t2 = float(input("Access time of Level 2 (t2, in microseconds) = "))

total_cost = c1 * s1 + c2 * s2
total_size = s1 + s2
avg_cost_per_bit = total_cost / total_size
avg_access_time = h * t1 + (1 - h) * t2

print(f"\nAverage Cost per Bit: {avg_cost_per_bit:.6f} INR")
print(f"Average Access Time: {avg_access_time:.6f} microseconds")
