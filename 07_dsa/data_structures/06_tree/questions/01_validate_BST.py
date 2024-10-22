
# Validate a Binary Search Tree (BST)
# Problem
# Determine if a given binary tree is a valid binary search tree.

# Solution: 
# Use a recursive approach to ensure that every node's value falls within a specific range defined by its ancestors.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, left=float('-inf'), right=float('inf')):
    if not root:
        return True
    if not (left < root.val < right):
        return False
    return (is_valid_bst(root.left, left, root.val) and
            is_valid_bst(root.right, root.val, right))
