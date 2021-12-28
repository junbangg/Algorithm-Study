/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */

 /// Iterative
 class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {
        var current = head
        var reversedHead: ListNode? = nil
        while current != nil {
            let temp = current?.next
            current!.next = reversedHead
            reversedHead = current
            current = temp
        }
        return reversedHead
    }
}

/// Recursive 
class Solution {
    func recurse(_ head: ListNode?, _ previous: ListNode? = nil) -> ListNode? {
        var head = head
        if head == nil {
            return previous
        }
        let next = head?.next
        head!.next = previous

        return recurse(next, head)
    }

    func reverseList(_ head: ListNode?) -> ListNode? {
        return recurse(head)
    }
}

