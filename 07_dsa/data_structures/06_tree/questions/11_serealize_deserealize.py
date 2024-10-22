
# Serialize and Deserialize Binary Tree

# Problem: 
# Design an algorithm to serialize and deserialize a binary tree.

# Solution: 
# Use a pre-order traversal for serialization and a queue for deserialization.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def serialize(root):
    def helper(node):
        if not node:
            vals.append("#")
        else:
            vals.append(str(node.val))
            helper(node.left)
            helper(node.right)
    vals = []
    helper(root)
    return ' '.join(vals)

def deserialize(data):
    def helper():
        val = next(vals)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()
