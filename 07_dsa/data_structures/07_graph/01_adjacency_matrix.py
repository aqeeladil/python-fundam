'''
Graph Representation
Graphs can be represented in two primary ways: Adjacency Matrix and Adjacency List.

Adjacency Matrix
An adjacency matrix is a 2D array of size 
𝑉×𝑉
V×V, where 𝑉 is the number of vertices in the graph. If there is an edge between vertex 
𝑖 and vertex 𝑗, then matrix[i][j] is 1 (or the weight of the edge, if it's a weighted graph), otherwise, it's 0.

Pros:
Simple and easy to implement.
Fast access to check if there is an edge between two vertices O(1).

Cons:
Consumes more space O(V^2)
Inefficient for sparse graphs where the number of edges E is much less than 𝑉^2

'''

def create_adjacency_matrix(vertices, edges):
    matrix = [[0] * vertices for _ in range(vertices)]
    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1  # For undirected graph
    return matrix

# Example usage
vertices = 5
edges = [(0, 1), (0, 2), (1, 3), (3, 4)]
adj_matrix = create_adjacency_matrix(vertices, edges)
for row in adj_matrix:
    print(row)
