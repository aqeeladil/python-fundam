# Heap Sort is a comparison-based sorting technique based on a binary heap data structure. 
# It first builds a max-heap and then repeatedly extracts the maximum element and reduces 
# the heap size.


# Time Complexity:

# Worst-case: O(n log n)
# Best-case: O(n log n)
# Average-case: O(n log n)
# Space Complexity: O(1) (in-place sorting)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
