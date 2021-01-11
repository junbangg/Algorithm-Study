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

    def iterative_inorder(self, root):
        current = root
        stack = []
        while 1:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data , end = " ")
                current = current.right
            else:
                break

    def get_count(self, root):
        count = 0
        if root:
            count = 1 + root.get_count(root.left) + root.get_count(root.right)
        return count

    def get_height(self, root):
        height = 0
        if root:
            height = 1 + max(root.get_height(root.left), root.get_height(root.right))
        return height

def copy(og):
    new = Node()
    if og:
        new.left = copy(og.left)
        new.right = copy(og.right)
        new.data = og.data
    return new

def is_equal(f, s):
    return not f and not s or f and s and f.data == s.data and is_equal(f.left, s.left) and is_equal(f.right, s.right)



root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
new.print_tree()
