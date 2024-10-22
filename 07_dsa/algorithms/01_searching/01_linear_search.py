# Complexity
# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(1), as it only requires a constant amount of extra space.

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


