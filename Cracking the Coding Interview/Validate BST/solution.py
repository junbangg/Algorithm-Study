# First attempt

# Approach. Traverse(inorder) tree and check left child is always <= than root
# and right child is always >= root

def validate(root):
    if root:
        if root.left and root.left.key > root.key:
            print("false")
            return False
        if root.right and root.right.key < root.key:
            print("false")
            return False
        return validate(root.left)
        return validate(root.right)


def solution(root):
    if validate(root) is None:
        return True
    else:
        return False


# Answer

