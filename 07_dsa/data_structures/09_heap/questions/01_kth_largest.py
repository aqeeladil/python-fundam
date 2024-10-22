

# Kth Largest Element in an Array

import heapq

def find_kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"{k}th largest element is {find_kth_largest(nums, k)}")


