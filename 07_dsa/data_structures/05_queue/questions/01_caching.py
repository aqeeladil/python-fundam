
# Caching
# Caching involves storing frequently accessed data in a faster storage medium (cache) 
# to reduce access time. A common implementation of a cache uses a queue with a limited size.

# Least Recently Used (LRU) Cache:
# An LRU cache removes the least recently used items when the cache reaches its limit. 
# This can be efficiently implemented using a combination of a deque and a dictionary.


from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


lru_cache = LRUCache(2)
lru_cache.put(1, 1)  # Cache is {1=1}
lru_cache.put(2, 2)  # Cache is {1=1, 2=2}
print(lru_cache.get(1))  # Returns 1, Cache is {2=2, 1=1}
lru_cache.put(3, 3)  # Evicts key 2, Cache is {1=1, 3=3}
print(lru_cache.get(2))  # Returns -1 (not found)
lru_cache.put(4, 4)  # Evicts key 1, Cache is {3=3, 4=4}
print(lru_cache.get(1))  # Returns -1 (not found)
print(lru_cache.get(3))  # Returns 3
print(lru_cache.get(4))  # Returns 4
