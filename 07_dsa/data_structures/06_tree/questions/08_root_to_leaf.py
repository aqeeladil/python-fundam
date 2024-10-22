
# Binary Tree Paths

# Problem: 
# Given a binary tree, return all root-to-leaf paths.

# Solution: 
# Use a DFS approach to explore all paths from the root to each leaf node.


def binary_tree_paths(root):
    def construct_paths(node, path):
        if node:
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                path += '->'
                construct_paths(node.left, path)
                construct_paths(node.right, path)
    paths = []
    construct_paths(root, '')
    return paths
