# first attempt
def check_balance(root):
    height = 0
    while root:
        lheight = check_balance(root.left)
        rheight = check_balance(root.right)
        if abs(lheight - rheight) > 1:
            return False
        height = 1 + max(lheight, rheight)
    return height


# def solution(root):
#    if checkBalance(root).is_integer():
#        return True
#    return False

# second attempt
def get_height(root):
    if root is None:
        return -1
    return 1+max(get_height(root.left), get_height(root.right))


def solution(root):  # probably wrong

    while root:
        dif = abs(get_height(root.left) - get_height(root.right))
        if dif > 1:
            return False
    return True


def solution2(root):
    if not root:
        return True
    dif = abs(get_height(root.left) - get_height(root.right))
    if dif > 1:
        return False
    return solution2(root.left) and solution2(root.right)
