def inorderSucc(n):
    if n.right:
        return leftMostChild(n.right)
    else:
        q = Node()
        q = n
        x = Node
        x = q.parent
        while x and x.left != q:
            q = x
            x = x.parent
        return x


def leftMostChild(n):
    if not n:
        return None
    while n.left:
        n = n.left
    return n
