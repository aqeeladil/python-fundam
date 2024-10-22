
# Longest Increasing Subsequence (LIS)

# Problem Statement: 
# Given an integer array, find the length of the longest increasing subsequence.

def lis(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(arr))  # Output: 6
