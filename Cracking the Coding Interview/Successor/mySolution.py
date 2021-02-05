def inorder(root, prev, val):
    if root:
        inorder(root, prev, val)
        if val == prev:
            return root.key
        else:
            prev = root.key
        inorder(root, prev, val)

    if root:
        if root.left and inorder(root.left, prev, val) == val:
            return root.val
        if root.right and inorder(root.right, prev, val) == val:
            return root.val
        return root.val


def mySolution(root, val):
    return inorder(root, None, val)


