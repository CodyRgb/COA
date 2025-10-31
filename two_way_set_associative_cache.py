import math

cache_kb = int(input("Enter size of Cache memory (in KB): "))
main_mb = int(input("Enter size of Main memory (in MB): "))
line_bytes = int(input("Enter size of each cache line (in Bytes): "))

cache_b = cache_kb * 1024
main_b = main_mb * 1024 * 1024
addr_bits = int(math.log2(main_b))
bank_size = cache_b
lines = bank_size // line_bytes
blocks = main_b // line_bytes
offset_bits = int(math.log2(line_bytes))
num_sets = lines // 2
set_bits = int(math.log2(num_sets))
tag_bits = addr_bits - (offset_bits + set_bits)

print("\nCache mapping policy: Two-Way Set Associative Mapping")
print(f"Number of sets = {num_sets} (Set No 0 to {num_sets - 1})")
print(f"Lines per set = 2")
print(f"Number of main memory blocks = {blocks} (Block No 0 to {blocks - 1})")

block_num = int(input("\nEnter any Main memory block number for cache mapping: "))
set_num = block_num % num_sets
print(f"\nBlock {block_num} is mapped into set number = {set_num}")
print("Block can be placed in either of the two lines in this set.")

print("\nMain memory address of", addr_bits, "bits is interpreted in 3 fields:")
print(f"LSB {offset_bits} bits for Byte selection")
print(f"Middle {set_bits} bits for Set selection")
print(f"MSB {tag_bits} bits for Tags")
