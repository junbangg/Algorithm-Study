# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# First Attempt (Naive)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        L = []
        p = head
        while p:
            L.append(p.val)
            p = p.next
        for i in range(1, len(L)):
            for j in range(i, 0, -1):
                if L[j-1] > L[j]:
                    L[j], L[j-1] = L[j-1], L[j]
        p = head
        for i in range(len(L)):
            p.val = L[i]
            p = p.next
        return head

# Second Attempt
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = root = ListNode()
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
            cur = root
        return cur.next
