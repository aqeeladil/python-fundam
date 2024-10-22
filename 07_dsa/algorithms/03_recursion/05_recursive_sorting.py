# Sort a list using the merge sort algorithm.

# Recursive Solution: Merge Sort is a divide-and-conquer algorithm that divides the list 
# into two halves, recursively sorts each half, and then merges the sorted halves.


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
print(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]))


