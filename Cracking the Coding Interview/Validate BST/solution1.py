# Approach:
# -1 Traverse(inorder) tree and save nodes to a list
# -2 check the list if it is sorted

def copy_to_list(root, vals):
    if root:
        copy_to_list(root.left, vals)
        vals.append(root.key)
        copy_to_list(root.right, vals)


def solution1(root):
    vals = []
    copy_to_list(root, vals)
    return vals == sorted(vals)
