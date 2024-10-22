# Count the Number of Rotations in a Rotated Sorted Array

# Count the number of rotations in a sorted array that has been rotated.

def count_rotations(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid - 1
    return low


arr = [15, 18, 2, 3, 6, 12]
print(count_rotations(arr))  # Output: 2


