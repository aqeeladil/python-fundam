

# Subarray Sum Equals K:

# Problem: Given an array of integers and an integer k, find the total number of continuous 
# subarrays whose sum equals to k.

# Solution: Use a hash map to store the cumulative sum up to each index and count the 
# occurrences of (cumulative_sum - k).


def subarray_sum(nums, k):
    count = 0
    cumulative_sum = 0
    hash_map = {0: 1}
    for num in nums:
        cumulative_sum += num
        if cumulative_sum - k in hash_map:
            count += hash_map[cumulative_sum - k]
        hash_map[cumulative_sum] = hash_map.get(cumulative_sum, 0) + 1
    return count

# Usage
print(subarray_sum([1, 1, 1], 2))  # Output: 2
