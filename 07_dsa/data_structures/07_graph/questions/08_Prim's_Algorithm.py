
# Minimum Spanning Tree (MST) Problems

# Problem 8: 
# Prim's Algorithm for MST

# Problem: Find the Minimum Spanning Tree (MST) of a graph using Prim's algorithm.



import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start]]
    heapq


