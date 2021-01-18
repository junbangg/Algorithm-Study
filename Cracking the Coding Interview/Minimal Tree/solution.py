# Minimal Tree: Given a sorted(increasing order) array with unique
# integer elements, write an algorithm to create a binary search tree with
# minimal height

class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key


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


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def solution(n):
    mid = len(n)//2-1
    arr = Node(n.pop(mid))
    for i in n:
        insert(arr, i)
    inorder(arr)


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n1 = [12, 46, 47, 80, 92, 100, 101, 155]
solution(n)
