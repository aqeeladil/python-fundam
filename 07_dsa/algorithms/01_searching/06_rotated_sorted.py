# Search in a Rotated Sorted Array

# Given a rotated sorted array, search for a target element. The array was originally sorted in 
# ascending order but then rotated at some pivot.

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


arr = [15, 18, 2, 3, 6, 12]
target = 3
print(search_rotated_array(arr, target))  # Output: 3


