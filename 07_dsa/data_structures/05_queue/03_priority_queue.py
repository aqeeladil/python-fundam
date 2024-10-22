# Priority Queue
'''
A Priority Queue is a type of queue where each element has a priority associated with it. 
Elements with higher priority are dequeued before elements with lower priority.
'''

# Key Operations:
'''
Insert (Enqueue): Insert an element with a priority.
Extract-Min/Max (Dequeue): Remove the element with the highest 
priority (or lowest, depending on implementation).
'''


# Implementation using a Min-Heap: (using Python's heapq module):
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        return heapq.heappop(self.heap)[1]

    def peek(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        return self.heap[0][1]

    def is_empty(self):
        return len(self.heap) == 0


