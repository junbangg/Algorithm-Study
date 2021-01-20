class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key


def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        elif root.val > key:
            root.left = insert(root.left, key)
    return root


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.left
            root = None
            return temp
        elif not root.right:
            temp = root.right
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)
