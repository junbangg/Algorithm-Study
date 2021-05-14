# Iterative Solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, rev = head, None
        while cur:
            rev, rev.next, cur= cur, rev, cur.next
        return rev

# Second Attempt
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast = head, head.next
        root = dummy = ListNode()
        while fast:
            slow.next, dummy.next, slow = dummy.next, slow, fast
            fast = fast.next
        if slow:
            slow.next, dummy.next = dummy.next, slow
        return root.next

# Recursive Solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node, prev = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)
