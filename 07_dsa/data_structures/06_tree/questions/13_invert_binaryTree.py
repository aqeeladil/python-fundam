
# Invert a Binary Tree

# Problem: 
# Invert a binary tree (mirror the tree).

# Solution: 
# Recursively swap the left and right children of each node.

def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
