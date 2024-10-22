
# Lowest Common Ancestor (LCA) of a Binary Search Tree
# Problem: 
# Given a BST, find the lowest common ancestor (LCA) of two given nodes.

# Solution: 
# Start from the root and move left or right depending on the values of the nodes until you find the LCA.


def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
