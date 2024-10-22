
# Arrays
- Operations (insert, delete, update, traverse)
- Two-pointer techniques

## Array Intro
- Linear data structure
- Array is a collection of items of the same variable type that are stored at contiguous memory locations.
- Each element has a unique index number.
- They have a fixed size, and accessing elements by index is efficient O(1) time complexity.However, inserting and deleting elements can be costly because elements may need to be shifted.

## Types of Arrays
- On the basis of size (fixed, dynamic)
- On the basis of dimensions (single, multi-dimensional(matrix))

## Applications of Array
- used to store multiple items of same type in continuous memory location
- Implementing queues, stacks, and other data structures
- Representing matrices and tables


## Disadvantages of array
- static array (memory wastage due to fixed size)
- homogenous (lack of flexibility to store different datatypes)

## Referential Arrays (call by reference/address)
- heterogenous (can store different datatypes)(unlike that of dynamic array in C++)
- more memory usage & speed is slow bcz here we are first accessing the address and then its actual item where it is pointing.

## Dynamic Arrays
- normally, dynamic array means collection of same type of elements, but in python, lists are dynamic as well as heterogenous. 
- dynamic array is just a concept. In memory, we simply just doubles the size of static array to create more space.


## Python Lists
- python lists are (referential + dynamic) arrays


## Two-Pointer Technique 
- Two pointers moving toward each other (e.g., searching for pairs that sum to a target).
- Two pointers moving at different speeds (e.g., detecting cycles in a linked list or removing duplicates).

## Common Two-Pointer Questions
- Given a string or array, reverse it using two pointers.
- Given two sorted arrays, find their intersection using the two-pointer technique.
- Given an unsorted array, find if there is a pair of elements that sum to a specific target.
- Merge two sorted arrays into one sorted array using the two-pointer approach.

## Benefits of the Two-Pointer Technique
- Reduces time complexity from O(n²) to O(n) in many cases.
- Efficient and straightforward for solving problems that involve arrays, linked lists, or strings.