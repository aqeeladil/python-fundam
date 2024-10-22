
# Breadth-First Search (BFS) Problems

# Problem 4: 
# Detect if a directed graph contains a cycle.

# Solution: 
# Use BFS (Kahn's Algorithm). If the number of visited nodes is less than the total number of nodes, a cycle exists.

from collections import deque, defaultdict

def detect_cycle_in_directed_graph(graph, vertices):
    indegree = {i: 0 for i in range(vertices)}
    
    for vertex in graph:
        for neighbor in graph[vertex]:
            indegree[neighbor] += 1
    
    queue = deque([v for v in indegree if indegree[v] == 0])
    count = 0
    
    while queue:
        vertex = queue.popleft()
        count += 1
        
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return count != vertices

# Example usage
graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]
}
print(detect_cycle_in_directed_graph(graph, 4))  # Output: True

