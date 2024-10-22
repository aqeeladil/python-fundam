# Rotate an array by k positions
# Given an array, rotate the array to the right by k steps.



def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # In case k is larger than the array size
    
    arr[:] = arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
rotate_array(arr, 3)
print(arr)



# T: O(n), S: O(1)