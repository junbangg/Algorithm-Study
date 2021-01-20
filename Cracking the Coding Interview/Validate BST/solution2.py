# Approach:
# in BSTs left.data <= root.data < right.data
# use Min and Max to keep track of the range
# in whether or not the BST condition above is met


def validate(root, minn, maxn):
    if not root:
        return True
    if minn and root.key < minn or maxn and root.key > maxn:
        return False
    if not validate(root.left, minn, root.key) or not validate(root.right, root.key, maxn):
        return False
    return True


def solution2(root):
    return validate(root, None, None)
