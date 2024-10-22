

# Depth-First Search (DFS) Problems

# Problem 1: 
# Find all connected components in an undirected graph.

# Solution: 
# Use DFS to explore each component.

def dfs(graph, vertex, visited, component):
    visited.add(vertex)
    component.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)

def find_connected_components(graph, vertices):
    visited = set()
    components = []
    
    for vertex in range(vertices):
        if vertex not in visited:
            component = []
            dfs(graph, vertex, visited, component)
            components.append(component)
    
    return components

# Example usage
graph = {
    0: [1],
    1: [0, 2, 3],
    2: [1],
    3: [1],
    4: [5],
    5: [4]
}
components = find_connected_components(graph, 6)
print(components)
