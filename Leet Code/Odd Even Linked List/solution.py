# naive solution
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        even, odd = [], []
        i = 0
        while head:
            if i % 2 == 0:
                odd.append(head.val)
            else:
                even.append(head.val)
            head = head.next
            i += 1
        arr = odd + even
        root = dummy= ListNode()
        for i in arr:
            temp = ListNode(i)
            dummy.next = temp
            dummy = dummy.next
        return root.next

# slow, fast approach
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenHead
        return head
