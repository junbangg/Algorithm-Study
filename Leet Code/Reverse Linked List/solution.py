class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, rev = head, None
        while cur:
            rev, rev.next, cur= cur, rev, cur.next
        return rev
