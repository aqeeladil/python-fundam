
# Two Sum Problem:

# Problem: 
# Given an array of integers, return indices of the two numbers such that they add up to a 
# specific target.

# Solution: Use a hash map to store the difference between the target and the current element.

def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num] = i
    return []

# Usage
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
