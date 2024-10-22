

# Hashing
- Hash tables, Hash maps
- Collision resolution techniques (separate chaining, open addressing)

## Intro
- Hashing is a technique that generates a fixed-size output (hash value) from an input of variable size using mathematical formulas called hash functions. 
- Hashing is used to determine an index or location for storing an item in a data structure, allowing for efficient retrieval and insertion.

## Key Concepts:
- Hash Function: A mathematical function that maps an input to a hash value.
- Hash Table: A data structure that stores key-value pairs, where the key is a hash value and the value is the actual data.
- Collision: When two different keys produce the same hash value.

## Collision Resolution Techniques:
- Separate Chaining (Open Hashing): Stores colliding elements in a linked list at the corresponding hash value.
- Open Addressing (Closed Hashing): Uses various strategies to find an alternative location for colliding elements within the hash table.

## Applications of Hashing:
- Efficiently storing and retrieving data in databases and file systems.
- Verifying passwords and digital signatures.
- Distributing requests across multiple servers.
- Generating secure hashes for data integrity and authentication.



