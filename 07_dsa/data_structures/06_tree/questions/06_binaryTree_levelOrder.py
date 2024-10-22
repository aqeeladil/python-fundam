
# Binary Tree Level Order Traversal

# Problem: 
# Return the level order traversal of a binary tree's nodes' values.

# Solution: 
# Use a queue to traverse the tree level by level.


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
