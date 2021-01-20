# First attempt

# Approach. Traverse(inorder) tree and check left child is always <= than root
# and right child is always >= root

def validate(root):
    if root:
        if root.left and root.left.key > root.key:
            return False
        if root.right and root.right.key < root.key:
            return False
        validate(root.left)
        validate(root.right)


def mySolution(root):
    if validate(root) is None:
        return True
    else:
        return False


# Answer

