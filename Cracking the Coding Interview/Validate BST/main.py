# 4.5 Validate BST: Implement a function to check if a Binary Tree is a BST.
# from mySolution import mySolution
# from solution1 import solution1
from solution2 import solution2


class Node():

    def __init__(self, val):
        self.left = None
        self.right = None
        self.key = val


# Regular Binary Tree
regularRoot = Node(30)
n2 = Node(15)
n3 = Node(60)
n4 = Node(7)
n5 = Node(27)
n6 = Node(45)
n7 = Node(75)
n8 = Node(17)
n9 = Node(22)
regularRoot.left = n2
regularRoot.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.left = n8
n5.right = n9


# Binary Search Tree
def insert(root, val):
    if not root:
        return Node(val)
    else:
        if root.key == val:
            return root
        elif root.key > val:
            root.left = insert(root.left, val)
        elif root.key < val:
            root.right = insert(root.right, val)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


vals = sorted([30, 15, 60, 7, 22, 17, 27, 45, 75])
midval = len(vals)//2
BSTroot = Node(vals.pop(midval))
for v in vals:
    insert(BSTroot, v)

# inorder(regularRoot)

# test mySolution -----------------------

# regular
# print(mySolution(regularRoot))
# BST
# print(solution(BSTroot))

# test solution1-----------------------

# regular
# print(solution1(regularRoot))
# BST
# print(solution1(BSTroot))

# test solution2----------------------

# regular
# print(solution2(regularRoot))
# BST
print(solution2(BSTroot))
