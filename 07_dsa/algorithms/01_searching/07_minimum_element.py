# Find Minimum Element in a Rotated Sorted Array

# Find the minimum element in a rotated sorted array. The array is originally sorted in 
# ascending order and then rotated.

def find_min_rotated_array(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return arr[low]


arr = [7, 9, 11, 12, 5]
print(find_min_rotated_array(arr))  # Output: 5


