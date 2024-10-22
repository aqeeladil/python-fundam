
# Flatten Binary Tree to Linked List

# Problem: 
# Flatten a binary tree to a linked list in place.

# Solution: 
# Use a post-order traversal and adjust the pointers to flatten the tree.

def flatten(root):
    if not root:
        return
    flatten(root.left)
    flatten(root.right)
    temp = root.right
    root.right = root.left
    root.left = None
    while root.right:
        root = root.right
    root.right = temp
