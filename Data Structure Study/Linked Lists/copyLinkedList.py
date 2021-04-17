class Node:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

def copyLinkedList(head):
    if not head:
        return head
    new_node = Node(head.val)
    new_node.next = copyLinkedList(head.next)
    return new_node
