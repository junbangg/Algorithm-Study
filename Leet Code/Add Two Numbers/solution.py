# Naive Approach
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # switch to lists
        lst1, lst2 = [], []
        while l1:
            lst1.append(l1.val)
            l1 = l1.next
        while l2:
            lst2.append(l2.val)
            l2 = l2.next
        num = int(''.join(map(str, lst1[::-1]))) + int(''.join(map(str, lst2[::-1])))
        nums = list(n for n in str(num))
        result = ListNode(int(nums.pop())) 
        ptr = result
        while nums:
            temp = ListNode(int(nums.pop()))
            ptr.next = temp
            ptr = ptr.next
        return result
# full adder approach 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next
