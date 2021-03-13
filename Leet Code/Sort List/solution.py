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
