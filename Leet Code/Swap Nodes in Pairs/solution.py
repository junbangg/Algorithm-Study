# Swaping values solution
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ptr = head
        while ptr and ptr.next:
            ptr.val, ptr.next.val = ptr.next.val, ptr.val
            ptr = ptr.next.next
        return head 

# Swapping node Solution
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None) 
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            
            prev.next = b
            
            head = head.next
            prev = prev.next.next
        return root.next
