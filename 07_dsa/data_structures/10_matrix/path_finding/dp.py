# Dynamic Programming (DP):
# DP is used for solving problems by breaking them down into simpler subproblems and 
# storing their results.
# In grids, DP can be used for problems like finding the minimum path sum or the number 
# of unique paths from one corner of the grid to another.


# Find the minimum path sum in a grid using dynamic programming.



def minPathSum(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Update the first column (only one way to move vertically down)
    for i in range(1, rows):
        grid[i][0] += grid[i-1][0]
    
    # Update the first row (only one way to move horizontally right)
    for j in range(1, cols):
        grid[0][j] += grid[0][j-1]
    
    # Update the rest of the grid by choosing the minimum path
    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    # The bottom-right corner contains the minimum path sum
    return grid[-1][-1]

# Example usage
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid))  # Output: 7
