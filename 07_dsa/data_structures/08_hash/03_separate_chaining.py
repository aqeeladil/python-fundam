
'''
Collision Resolution Techniques
Collisions occur when the hash function generates the same index for more than one key. 
There are two primary methods to resolve collisions: separate chaining and open addressing.

Separate Chaining
In separate chaining, each index in the hash table's array points to a linked list 
(or another data structure, like a binary search tree). All elements that hash to the 
same index are stored in this list.

Advantages:
Simple to implement.
Can handle a large number of collisions efficiently.

Disadvantages:
Extra memory for pointers (in linked lists).
Performance degrades as the number of collisions increases.

'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

# Usage
hash_table = HashTable(10)
hash_table.insert("apple", 100)
hash_table.insert("banana", 200)
print(hash_table.search("apple"))  # Output: 100
