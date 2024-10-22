
# Shortest Path Algorithms
# Bellman-Ford Algorithm
# Bellman-Ford is used for finding the shortest path in graphs with negative weights. 
# It can detect negative weight cycles.


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
distances = bellman_ford(edges, vertices, 0)
print(distances)
