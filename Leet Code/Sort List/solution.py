# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        length = 0
        arr = []
        # create temp list and count length of list
        while head:
            length += 1
            arr.append(head.val)
            head = head.next
        # quick sort
        def quickSort(arr, low, high):
            def partition(low, high):
                pivot = arr[high]
                left = low
                for right in range(high):
                    if arr[left] < pivot:
                        arr[left], arr[right] = arr[right], arr[left]
                arr[left], arr[high] = arr[left], arr[high]
                return left
            if low < high:
                pivot = partition(low, high)
                quickSort(arr, low, pivot-1)
                quickSort(arr, pivot, high)
            return arr

