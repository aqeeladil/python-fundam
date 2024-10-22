
# Symmetric Tree

# Problem: 
# Check if a binary tree is symmetric around its center.

# Solution: 
# Use a recursive approach to compare the left and right subtrees for symmetry.


def is_symmetric(root):
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))
    return is_mirror(root, root)
