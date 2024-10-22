
# Top K Frequent Elements:

# Problem: Given a non-empty array of integers, return the k most frequent elements.

# Solution: Use a hash map to count the frequency of each element, then use a heap or 
# bucket sort to find the top k elements.

from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Usage
print(top_k_frequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
