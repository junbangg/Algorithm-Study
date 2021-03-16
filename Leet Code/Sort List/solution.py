# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        arr = []
        while p:
            arr.append(p.val)
            p= p.next
        arr.sort()
        p = head
        for i in range(len(arr)):
            p.val = arr[i]
            p = p.next
        return head

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        # edge case
        if not (head and head.next):
            return head
        # Runner 기법
        mid, slow, fast = None, head, head
        while fast and fast.next:
            mid, slow, fast = slow, slow.next, fast.next.next
        mid.next = None
        # 분할 재귀 호출 
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        # 합병
        return self.mergeTwoLists(l1, l2)

