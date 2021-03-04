class ListNode:
    
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # if not in table
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        # if already in table
        cur = self.table[index]
        while cur:
            if cur.key == key:
                cur.value = value
                return
            if cur.next is None:
                break
            cur = cur.next
        cur.next = ListNode(key, value) 
               

    def get(self, key: int) -> int:
        index = key % self.size
        # if not in table
        if self.table[index].value is None:
            return -1
        # if already in table
        cur = self.table[index]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1            

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        # when first index
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        # remove from linked list
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
