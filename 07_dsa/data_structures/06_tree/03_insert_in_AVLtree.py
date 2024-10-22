# Insert a node in an AVL tree

class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1

def insert(root, key):
    if not root:
        return AVLNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)
    # Perform rotations if necessary
    return balance_tree(root, key)

def balance_tree(root, key):
    balance = get_balance(root)
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root
