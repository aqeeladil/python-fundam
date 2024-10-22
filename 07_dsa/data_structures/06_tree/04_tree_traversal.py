
# Inorder (Left, Root, Right): 
# For a BST, this yields nodes in non-decreasing order.
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


# Preorder (Root, Left, Right): 
# Used to create a copy of the tree.
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


# Postorder (Left, Right, Root): 
# Used to delete or free nodes in the tree.
def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []
