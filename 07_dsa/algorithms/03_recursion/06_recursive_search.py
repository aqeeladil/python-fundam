# Recursive Searching (Binary Search)
# Problem Statement: Search for a target value in a sorted list using binary search.

# Recursive Solution: Binary search involves recursively dividing the list in half 
# and comparing the target value to the middle element.


def binary_search(lst, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, high)
    else:
        return binary_search(lst, target, low, mid - 1)

# Example usage
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(sorted_list, 5, 0, len(sorted_list) - 1))
