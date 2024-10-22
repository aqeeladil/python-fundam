# Iteratively compares adjacent elements and swaps them if they are out of order. 
# The largest element “bubbles” to the end of the list with each pass.

# Time Complexity:

# Worst-case: O(n²)
# Best-case: O(n) (when the array is already sorted)
# Average-case: O(n²)
# Space Complexity: O(1) (in-place sorting)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


