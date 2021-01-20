# First attempt

# Approach. Traverse(inorder) tree and check left child is always <= than root
# and right child is always >= root


def mySolution(root):
    if not root:
        return True
    if root.left and root.left.key > root.key or root.right and root.right.key < root.key:
        return False
    if not validate(root.left) or not validate(root.right):
        return False
    return True
