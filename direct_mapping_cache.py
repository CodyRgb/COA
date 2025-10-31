class DirectMappingCache:
    """Simulates a direct mapping cache."""
    def __init__(self, cache_size: int, block_size: int):
        if not (cache_size > 0 and cache_size & (cache_size - 1) == 0):
            raise ValueError("Cache size must be a power of 2")
        if not (block_size > 0 and block_size & (block_size - 1) == 0):
            raise ValueError("Block size must be a power of 2")
        self.cache_size = cache_size
        self.block_size = block_size
        self.num_blocks = cache_size // block_size
        self.cache = [None] * self.num_blocks

    def access(self, address: int) -> str:
        """Accesses a memory address and returns 'Hit' or 'Miss'."""
        block_number = address // self.block_size
        cache_index = block_number % self.num_blocks
        tag = block_number // self.num_blocks

        if self.cache[cache_index] is not None and self.cache[cache_index]['tag'] == tag:
            return "Hit"
        else:
            self.cache[cache_index] = {'tag': tag, 'data': f"data for address {address}"}
            return "Miss"

if __name__ == '__main__':
    try:
        cache_s = int(input("Enter cache size (power of 2): "))
        block_s = int(input("Enter block size (power of 2): "))
        cache = DirectMappingCache(cache_s, block_s)
        while True:
            addr_str = input("Enter memory address to access (or 'q' to quit): ")
            if addr_str.lower() == 'q':
                break
            address = int(addr_str)
            result = cache.access(address)
            print(f"Address {address}: {result}")
            print(f"Cache state: {cache.cache}")
    except ValueError as e:
        print(f"Error: {e}")