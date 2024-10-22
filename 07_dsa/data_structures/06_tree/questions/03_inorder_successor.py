'''
Inorder Successor in a BST

Problem: 
Given a BST and a node, find the inorder successor of that node.

Solution: 
If the node has a right subtree, the successor is the leftmost node of the right subtree. 
If it doesn’t have a right subtree, move up the tree to find the first ancestor for which 
the node is in the left subtree.
'''


def inorder_successor(root, p):
    successor = None
    while root:
        if p.val < root.val:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor
