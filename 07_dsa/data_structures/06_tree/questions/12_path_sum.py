
# Path Sum
# Problem: 
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that 
# adding up all the values along the path equals the given sum.

# Solution: 
# Use DFS to check each path from root to leaf.

def has_path_sum(root, sum):
    if not root:
        return False
    sum -= root.val
    if not root.left and not root.right:
        return sum == 0
    return has_path_sum(root.left, sum) or has_path_sum(root.right, sum)

