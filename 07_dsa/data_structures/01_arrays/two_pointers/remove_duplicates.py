# Given a sorted array, remove the duplicates in place such that each element appears 
# only once and return the new length.


def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    # return the new length.
    return slow + 1

# Example usage
arr = [1, 1, 2, 2, 3]
length = remove_duplicates(arr)
print(arr[:length])  # Output: [1, 2, 3]


# Time Complexity: O(n), where n is the length of the array.


