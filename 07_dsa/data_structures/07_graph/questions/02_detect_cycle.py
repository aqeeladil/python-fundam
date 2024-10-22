
# Depth-First Search (DFS) Problems

# Problem 2: 
# Determine if a cycle exists in an undirected graph.

# Solution: 
# Use DFS to check for back edges.

def is_cyclic_dfs(graph, vertex, visited, parent):
    visited.add(vertex)
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if is_cyclic_dfs(graph, neighbor, visited, vertex):
                return True
        elif parent != neighbor:
            return True
    
    return False

def has_cycle(graph, vertices):
    visited = set()
    
    for vertex in range(vertices):
        if vertex not in visited:
            if is_cyclic_dfs(graph, vertex, visited, -1):
                return True
    
    return False

# Example usage
graph = {
    0: [1],
    1: [0, 2, 3],
    2: [1, 3],
    3: [1, 2],
    4: [5],
    5: [4]
}
print(has_cycle(graph, 6))  # Output: True
