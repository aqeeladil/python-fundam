# Find the First Occurrence of an Element in an Unsorted List

# Given an unsorted list of integers, find the index of the first occurrence of a 
# specific element.


def find_first_occurrence(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


arr = [4, 2, 5, 2, 7]
target = 2
print(find_first_occurrence(arr, target))  # Output: 1

