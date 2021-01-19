from solution import solution2


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


root = Node(1)
root.insert(2)
root.insert(5)
root.insert(6)
root.insert(23)
root.insert(3)
root.insert(29)
root.insert(12)
root.insert(24)
root.insert(13)

print(solution2(root))
