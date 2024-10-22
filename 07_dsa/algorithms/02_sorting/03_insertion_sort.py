# Builds the sorted list one element at a time by inserting each unsorted element 
# into its correct position in the sorted portion.

# Time Complexity:

# Worst-case: O(n²)
# Best-case: O(n) (when the array is already sorted)
# Average-case: O(n²)
# Space Complexity: O(1) (in-place sorting)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
