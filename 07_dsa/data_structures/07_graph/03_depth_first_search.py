
# Depth-First Search (DFS)
# DFS is a traversal technique that explores as far as possible along each branch before backing up. 
# It uses a stack (either explicitly or through recursion).

from collections import defaultdict

def create_adjacency_list(vertices, edges):
    adj_list = defaultdict(list)
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)  # For undirected graph
    return adj_list

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = create_adjacency_list(5, [(0, 1), (0, 2), (1, 3), (3, 4)])
dfs(graph, 0)
