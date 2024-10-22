
# Breadth-First Search (BFS)
# BFS explores all the neighbors at the present depth before moving on to nodes at the next depth level. 
# It uses a queue to maintain the order of traversal.

from collections import deque
from collections import defaultdict


def create_adjacency_list(vertices, edges):
    adj_list = defaultdict(list)
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)  # For undirected graph
    return adj_list


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
graph = create_adjacency_list(5, [(0, 1), (0, 2), (1, 3), (3, 4)])
bfs(graph, 0)
