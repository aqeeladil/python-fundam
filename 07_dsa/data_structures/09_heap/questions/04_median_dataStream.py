
# Find Median from Data Stream

import heapq

class MedianFinder:
    def __init__(self):
        self.low = []  # Max-Heap
        self.high = [] # Min-Heap
    
    def addNum(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))
    
    def findMedian(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2.0

# Example usage
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print("Median:", medianFinder.findMedian())
medianFinder.addNum(3)
print("Median:", medianFinder.findMedian())


