def search_rotated_array(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:  # Left half is sorted
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


# Linear Search: Simple but inefficient for large lists; best for unsorted or small data.
# Binary Search: Efficient but requires sorted data; very fast for large lists.
# Search in Rotated Array: Efficiently searches in arrays that are sorted but rotated, 
# combining binary search with rotation handling.