
# Minimum Spanning Trees

# Kruskal's Algorithm
# Kruskal’s algorithm finds a minimum spanning tree for a graph by sorting all the edges and 
# adding them one by one to the spanning tree if they don’t form a cycle.

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(vertices, edges):
    result = []
    i = 0
    e = 0
    edges = sorted(edges, key=lambda item: item[2])
    parent = []
    rank = []
    
    for node in range(vertices):
        parent.append(node)
        rank.append(0)
    
    while e < vertices - 1:
        u, v, w = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            e = e + 1
            result.append((u, v, w))
            union(parent, rank, x, y)
    
    return result

# Example usage
vertices = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
mst = kruskal(vertices, edges)
print(mst)
