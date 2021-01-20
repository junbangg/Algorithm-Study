# Approach:
# in BSTs left.data <= root.data < right.data
# use Min and Max to keep track of the range
# in whether or not the BST condition above is met


def validate(root, minn, maxn):
    if not root:
        return True
    if minn and root.val < minn or maxn and root.val > maxn:
        return False
    if !validate(root.left, minn, root.val) or !validate(root.right, root.val, maxn):
        return False
    return True


def solution(root):
    return validate(root, None, None)
