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
line_bits = int(math.log2(cache_lines))
tag_bits = address_bits - (byte_bits + line_bits)

print("\nCache mapping policy: Direct Mapping")
print(f"Main Memmory Address = {address_bits}")
print(f"Number of cache banks = {cache_banks}")
print(f"Hence, size of cache bank = {cache_bank_size // 1024} KB")
print(f"Cache lines per cache bank = {cache_lines} (Line No 0 to {cache_lines - 1})")
print(f"Number of main memory blocks = {main_blocks} (Block No 0 to {main_blocks - 1})")

block_num = int(input("\nEnter any Main memory block number for cache mapping: "))
cache_line = block_num % cache_lines
print(f"\nBlock {block_num} is mapped into cache line number = {cache_line}")

print("\nMain memory address of", address_bits, "bits is interpreted in 3 fields:")
print(f"LSB {byte_bits} bits for Byte selection")
print(f"Middle {line_bits} bits for Cache line selection")
print(f"MSB {tag_bits} bits for Tags")