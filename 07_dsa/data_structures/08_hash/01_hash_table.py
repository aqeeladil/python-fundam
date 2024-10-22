
'''
A hash table is a data structure that stores key-value pairs. It uses a hash function to 
compute an index (also known as a hash code) into an array of buckets or slots, from which 
the desired value can be found.


Average Time Complexity: 
O(1) for insertion, deletion, and lookup (in the case of a good hash function and low 
collision rate).

Worst Time Complexity: 
O(n) in case of many collisions and a poor hash function.

'''

def simple_hash(key, table_size):
    return sum(ord(char) for char in key) % table_size
