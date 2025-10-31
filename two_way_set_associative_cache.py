class TwoWaySetAssociativeCache:
    """Simulates a 2-way set associative cache."""
    def __init__(self, cache_size: int, block_size: int):
        if not (cache_size > 0 and cache_size & (cache_size - 1) == 0):
            raise ValueError("Cache size must be a power of 2")
        if not (block_size > 0 and block_size & (block_size - 1) == 0):
            raise ValueError("Block size must be a power of 2")
        self.cache_size = cache_size
        self.block_size = block_size
        self.num_sets = cache_size // (block_size * 2)
        self.cache = [[None, None] for _ in range(self.num_sets)]
        self.lru = [[0, 1] for _ in range(self.num_sets)]

    def access(self, address: int) -> str:
        """Accesses a memory address and returns 'Hit' or 'Miss'."""
        block_number = address // self.block_size
        set_index = block_number % self.num_sets
        tag = block_number // self.num_sets

        for i in range(2):
            if self.cache[set_index][i] is not None and self.cache[set_index][i]['tag'] == tag:
                self.lru[set_index] = [i, 1 - i]
                return "Hit"

        replace_index = self.lru[set_index][1]
        self.cache[set_index][replace_index] = {'tag': tag, 'data': f"data for address {address}"}
        self.lru[set_index] = [replace_index, 1 - replace_index]
        return "Miss"

if __name__ == '__main__':
    try:
        cache_s = int(input("Enter cache size (power of 2): "))
        block_s = int(input("Enter block size (power of 2): "))
        cache = TwoWaySetAssociativeCache(cache_s, block_s)
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