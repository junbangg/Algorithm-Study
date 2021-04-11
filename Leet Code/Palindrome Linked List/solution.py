# Deque solution
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        d = collections.deque()
        while cur:
            d.append(cur.val)
            cur = cur.next
        while True: 
            if len(d) >= 2:
                if d[0] == d[-1]:
                    d.popleft()
                    d.pop()
                else:
                    break
            if len(d) <= 1:
                return True
        return d == []
# Deque solution trimmed down
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        d = collections.deque()
        while cur:
            d.append(cur.val)
            cur = cur.next
        while len(d) > 1:
            if d.popleft() != d.pop():
                return False
        return True

# Check reversed linked list
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
