# Counting Sort is a non-comparison-based sorting algorithm that counts the number 
# of occurrences of each distinct element in the array. It then uses this count to 
# place the elements in their correct position.

# Time Complexity:

# Worst-case: O(n + k) (where k is the range of the input elements)
# Best-case: O(n + k)
# Average-case: O(n + k)
# Space Complexity: O(n + k)

def counting_sort(arr):
    max_element = max(arr)
    min_element = min(arr)
    range_of_elements = max_element - min_element + 1
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    for i in range(len(arr)):
        count_arr[arr[i] - min_element] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]
