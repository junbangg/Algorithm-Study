class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:

            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()

        print(self.data)

        if self.right:
            self.right.print_tree()

    def preorder(self, root):
        if root:
            print(root.data)
            root.preorder(root.left)
            root.preorder(root.right)

    def inorder(self, root):
        if root:
            root.inorder(root.left)
            print(root.data)
            root.inorder(root.right)
    
    def postorder(self, root):
        if root:
            root.postorder(root.left)
            root.postorder(root.right)
            print(root.data)

        


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))
