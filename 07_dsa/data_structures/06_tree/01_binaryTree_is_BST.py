
# Check if a Binary Tree is a BST
def is_bst(node, left=float('-inf'), right=float('inf')):
    if not node:
        return True
    if not (left < node.val < right):
        return False
    return is_bst(node.left, left, node.val) and is_bst(node.right, node.val, right)

