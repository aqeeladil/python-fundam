
# Minimum Spanning Trees

# Prim's Algorithm
# Prim’s algorithm builds the minimum spanning tree by adding vertices to the tree one by one, 
# starting from an arbitrary vertex and always choosing the smallest edge that connects a vertex 
# inside the tree to one outside it.


import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start]]
    heapq.heapify(edges)
    
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            
            for to_next, cost in graph[to]:
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))
    
    return mst


