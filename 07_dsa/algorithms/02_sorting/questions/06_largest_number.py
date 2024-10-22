# Given a list of non-negative integers, arrange them such that they form the largest number.

from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1
    else:
        return 1

def largest_number(nums):
    nums_str = list(map(str, nums))
    nums_str.sort(key=cmp_to_key(compare))
    largest_num = ''.join(nums_str)
    return '0' if largest_num[0] == '0' else largest_num

# Example usage:
nums = [3, 30, 34, 5, 9]
print(largest_number(nums))  # Output: "9534330"


