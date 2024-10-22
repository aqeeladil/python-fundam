
# Given a sorted array of integers, find two numbers that add up to a specific target number. 
# Return the indices of the two numbers.


def two_sum_sorted(arr, target):

    # Sort the array
    arr.sort()

    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]  # No solution found

# Example usage
arr = [2, 3, 4, 7, 11, 15]
target = 9
result = two_sum_sorted(arr, target)
print(result)  # Output: [0, 3]



# If array is unsorted

def twoSum(nums, target):

    prevMap = {} # val : index

    for i, n in enumerate(nums):
        diff = target - n

        if diff in prevMap:
            return [prevMap[diff], i]
                
        prevMap[n] = i

    return None




