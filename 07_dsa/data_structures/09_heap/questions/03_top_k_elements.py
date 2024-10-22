

# Top K Frequent Elements

import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    heap = []
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for freq, num in heap]

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(f"Top {k} frequent elements are {top_k_frequent(nums, k)}")
