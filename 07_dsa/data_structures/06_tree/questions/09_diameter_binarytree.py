
# Diameter of a Binary Tree
# Problem: 
# Find the diameter of a binary tree, which is the length of the longest path between any two nodes in the tree.

# Solution: 
# Use DFS to calculate the height of each subtree and track the maximum diameter found.


def diameter_of_binary_tree(root):
    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    diameter = 0
    depth(root)
    return diameter

