
'''
Adjacency List
An adjacency list represents the graph as an array of lists. The array index represents a vertex, and the list at that index contains the vertices it is connected to.

Pros:
Space-efficient O(V+E) for sparse graphs.
Easier to iterate over all adjacent vertices.

Cons:
Checking the existence of a specific edge takes O(V) time in the worst case.

'''
from collections import defaultdict

def create_adjacency_list(vertices, edges):
    adj_list = defaultdict(list)
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)  # For undirected graph
    return adj_list

# Example usage
vertices = 5
edges = [(0, 1), (0, 2), (1, 3), (3, 4)]
adj_list = create_adjacency_list(vertices, edges)
for vertex in adj_list:
    print(vertex, "->", adj_list[vertex])
