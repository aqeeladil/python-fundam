
# Level Order Traversal (Breadth-First Search):
from collections import deque

def level_order(root):
    levels = []
    if not root:
        return levels
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
    return levels


