
'''
Collision Resolution Techniques
Collisions occur when the hash function generates the same index for more than one key. 
There are two primary methods to resolve collisions: separate chaining and open addressing.

Open Addressing
In open addressing, all elements are stored directly in the array. If a collision occurs, the algorithm searches for the next available slot according to a probing sequence.

Types of Probing:

Linear Probing: If the index i is occupied, try i+1, i+2, and so on.
Quadratic Probing: Use a quadratic function to calculate the next slot, e.g., i+1^2, i+2^2.
Double Hashing: Use a second hash function to calculate the offset for probing.

Advantages:
No extra memory is needed for pointers.
All data is stored in a contiguous block of memory.

Disadvantages:
Primary clustering (especially in linear probing).
Decreased performance as the load factor increases.

'''
# Example of Linear Probing:

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                return None
        return None

# Usage
hash_table = HashTable(10)
hash_table.insert("apple", 100)
hash_table.insert("banana", 200)
print(hash_table.search("apple"))  # Output: 100
