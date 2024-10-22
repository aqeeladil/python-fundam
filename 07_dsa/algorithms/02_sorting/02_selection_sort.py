# Finds the minimum element in the unsorted portion of the list and 
# swaps it with the first element. Repeats this process until the entire list is sorted.

# Time Complexity:

# Worst-case: O(n²)
# Best-case: O(n²)
# Average-case: O(n²)
# Space Complexity: O(1) (in-place sorting)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
