
# Maximum Depth of a Binary Tree

# Problem: 
# Find the maximum depth (or height) of a binary tree.

# Solution: 
# Use a depth-first search (DFS) approach to calculate the depth of the tree.

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
