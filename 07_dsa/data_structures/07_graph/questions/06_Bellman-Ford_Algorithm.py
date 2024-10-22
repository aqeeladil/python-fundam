
# Shortest Path Problems


# Problem 6: 
# Bellman-Ford Algorithm for Shortest Path with Negative Weights
    
# Problem: Find the shortest path from a source vertex to all other vertices in a graph with 
# negative weights and detect negative weight cycles.

def bellman_ford(graph, vertices, start):
    distances = {vertex: float('infinity') for vertex in range(vertices)}
    distances[start] = 0
    
    for _ in range(vertices - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative-weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            print("Graph contains a negative-weight cycle")
            return None
    
    return distances

# Example usage
vertices = 5
edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (3, 4, 3), (3, 2, -10)]
print(bellman_ford(edges, vertices, 0))
