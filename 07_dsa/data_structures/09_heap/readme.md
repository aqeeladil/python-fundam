

# Heaps
- Min-Heap, Max-Heap, Heap Sort
- Priority Queue

## Intro
- A Heap is a complete binary tree data structure that satisfies the heap property: for every node, the value of its children is less than or equal to its own value. 
- Heaps are usually used to implement priority queues, where the smallest (or largest) element is always at the root of the tree.

## Operations of Heap:
- Insert: Adds a new element to the heap while maintaining heap properties.
- Extract-Max/Extract-Min: Removes the root element and restructures the heap.
- Increase/Decrease-Key: Updates the value of a node and restructures the heap.

## Types of Heap:
- Max-Heap: Root node has the maximum value among its children.
- Min-Heap: Root node has the minimum value among its children.

## Heap Sort
- Heap Sort is a comparison-based sorting algorithm that uses the properties of a heap to sort elements. It works as follows:
- Build a Max-Heap from the input data.
- Repeatedly extract the maximum element (the root) and move it to the end of the array.
- Reduce the size of the heap and heapify the root to maintain the heap property.
- This process is repeated until all elements are sorted.

## Priority Queue
- A Priority Queue is an abstract data type similar to a regular queue, but with each element having a priority. Elements with higher priority are dequeued before elements with lower priority. Heaps are often used to implement priority queues.

- Min-Priority Queue: The element with the lowest priority is at the root (smallest value has the highest priority).
- Max-Priority Queue: The element with the highest priority is at the root (largest value has the highest priority).

## Applications of Heap:
- Priority queues
- Sorting
- Graph algorithms (e.g., Dijkstra’s algorithm)