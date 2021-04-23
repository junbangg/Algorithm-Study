# Iterative Solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, rev = head, None
        while cur:
            rev, rev.next, cur= cur, rev, cur.next
        return rev

# Recursive Solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node, prev = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)
