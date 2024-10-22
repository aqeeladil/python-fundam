# Breadth-First Search (BFS):
# BFS explores all nodes at the present depth before moving on to nodes at the next depth level.
# BFS is commonly used for finding the shortest path in an unweighted grid or maze.

# Find the shortest path in a binary maze using BFS.

from collections import deque

def bfs_shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == end:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 0  # mark as visited
                queue.append((nr, nc, dist + 1))
    
    return -1  # no path found

# Example usage
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
start = (0, 0)
end = (3, 3)
print(bfs_shortest_path(maze, start, end))  # Output: 5

