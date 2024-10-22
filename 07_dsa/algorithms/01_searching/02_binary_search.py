# Complexity
# Time Complexity: O(log n), where n is the number of elements in the list.
# Space Complexity: O(1) for iterative implementation and O(log n) for recursive implementation.


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


