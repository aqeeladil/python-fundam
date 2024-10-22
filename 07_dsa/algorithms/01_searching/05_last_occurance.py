
# Find the Last Occurrence of an Element in a Sorted List

# Given a sorted list of integers with duplicates, find the index of the last occurrence 
# of a specific element.


def find_last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


arr = [1, 2, 2, 2, 3, 4]
target = 2
print(find_last_occurrence(arr, target))  # Output: 3