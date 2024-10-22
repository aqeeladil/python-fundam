# Radix Sort sorts numbers by processing individual digits. It sorts the array based 
# on each digit starting from the least significant digit (LSD) to the most significant digit (MSD).



# Time Complexity:

# Worst-case: O(nk) (where n is the number of elements and k is the number of digits)
# Best-case: O(nk)
# Average-case: O(nk)
# Space Complexity: O(n + k)


def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_element = max(arr)
    exp = 1
    while max_element // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10


