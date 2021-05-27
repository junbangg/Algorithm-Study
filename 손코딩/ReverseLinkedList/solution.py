
a -> b -> c -> d -> e -> None

prev = None
node = a
node.next = b
b           None
nextNode, node.next = node.next, prev
a       b
prev, node = node, nextNode


e -> d -> c -> b -> a -> None

def reverseLinkedList(head):
    node, prev = head, None
    while node:
        nextNode, node.next = node.next, prev
        prev, node = node, nextNode
    return prev


