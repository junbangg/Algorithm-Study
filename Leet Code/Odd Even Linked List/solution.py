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
