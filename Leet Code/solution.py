class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) == self.size:
            return False
        self.queue.append(value)
        return True

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.pop(0)
            return True
        return False

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.queue) == self.size:
            return True
        return False
