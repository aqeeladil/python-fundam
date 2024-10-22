
# Breadth-First Search (BFS)
'''
BFS is a graph traversal algorithm that explores all vertices at the present depth level 
before moving on to vertices at the next depth level. It uses a queue to keep track of 
vertices to visit next.
'''

# Algorithm:
'''
Initialize a queue and enqueue the starting vertex.
Mark the starting vertex as visited.
While the queue is not empty:
Dequeue a vertex from the queue.
Visit all its adjacent vertices that haven’t been visited.
Mark these vertices as visited and enqueue them.
'''


from collections import deque

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

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
# Output: A B C D E F


