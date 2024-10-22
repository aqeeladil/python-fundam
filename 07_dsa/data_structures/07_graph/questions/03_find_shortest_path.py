

# Breadth-First Search (BFS) Problems

# Problem 3: 
# Find the shortest path from a source vertex to all other vertices in an unweighted graph.

# Solution: 
# Use BFS, as it explores the graph level by level.

from collections import deque

def bfs_shortest_path(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if distances[neighbor] == float('infinity'):
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    return distances

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3]
}
print(bfs_shortest_path(graph, 0))
