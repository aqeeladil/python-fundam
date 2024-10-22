

# Priority Queue Using Min-Heap

import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def insert(self, item):
        heapq.heappush(self.pq, item)

    def extract_min(self):
        return heapq.heappop(self.pq)

    def peek(self):
        return self.pq[0] if self.pq else None

pq = PriorityQueue()
pq.insert(3)
pq.insert(1)
pq.insert(2)
print("Min element:", pq.extract_min())
