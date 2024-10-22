

# Matrix Chain Multiplication

# Problem Statement: 
# Given a sequence of matrices, find the most efficient way to multiply these matrices together.
# The problem is to find the minimum number of scalar multiplications needed.


def matrix_chain_multiplication(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[0][n - 1]

# Example usage
p = [10, 20, 30, 40, 30]
print(matrix_chain_multiplication(p))  # Output: 30000
