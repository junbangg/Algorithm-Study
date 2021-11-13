import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    print(node.data, end = '')
    if node.left:
        preorder(binaryTree[node.left])
    if node.right:
        preorder(binaryTree[node.right])

def inorder(node):
    if node.left:
        inorder(binaryTree[node.left])
    print(node.data, end = '')
    if node.right:
        inorder(binaryTree[node.right])

def postorder(node):
    if node.left:
        postorder(binaryTree[node.left])
    if node.right:
        postorder(binaryTree[node.right])
    print(node.data, end = '')

N = int(input())
binaryTree = {}
for _ in range(N):
    letter, left, right = input().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    binaryTree[letter] = Node(data = letter, left = left, right = right)

preorder(binaryTree['A'])
print()
inorder(binaryTree['A'])
print()
postorder(binaryTree['A'])