import math

cache_size_kb = int(input("Enter size of Cache memory (in KB): "))
main_size_mb = int(input("Enter size of Main memory (in MB): "))
line_size = int(input("Enter size of each cache line (in Bytes): "))

cache_size = cache_size_kb * 1024
main_size = main_size_mb * 1024 * 1024
address_bits = int(math.log2(main_size))
cache_banks = 1
cache_bank_size = cache_size // cache_banks
cache_lines = cache_bank_size // line_size
main_blocks = main_size // line_size
byte_bits = int(math.log2(line_size))
sets = cache_lines // 2
set_bits = int(math.log2(sets))
tag_bits = address_bits - (byte_bits + set_bits)

print("\nCache mapping policy: Two-Way Set Associative Mapping")
print(f"Number of sets = {sets} (Set No 0 to {sets - 1})")
print(f"Lines per set = 2")
print(f"Number of main memory blocks = {main_blocks} (Block No 0 to {main_blocks - 1})")

block_num = int(input("\nEnter any Main memory block number for cache mapping: "))
set_number = block_num % sets
print(f"\nBlock {block_num} is mapped into set number = {set_number}")
print("Block can be placed in either of the two lines in this set.")

print("\nMain memory address of", address_bits, "bits is interpreted in 3 fields:")
print(f"LSB {byte_bits} bits for Byte selection")
print(f"Middle {set_bits} bits for Set selection")
print(f"MSB {tag_bits} bits for Tags")
