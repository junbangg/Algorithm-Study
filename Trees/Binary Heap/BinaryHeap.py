import sys

class BinaryHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.Front = 1

    #Index Functions
    def parent(self, pos):
        return pos//2

    def rchild(self, pos):
        return 2 * pos + 1

    def lchild(self, pos):
        return 2 * pos

    #Check if node is Leaf
    def isLeaf(self, pos):
        if pos >= self.size//2 and pos <= self.size:
            return True
        return False

    #Swap function
    def swap(self, first, second):
        self.Heap[first] , self.Heap[second] = self.Heap[second], self.Heap[first]

    #Heapify
    def minHeapify(self, pos):
        #단말 노드(leaf) 가 아니고, child 노드 둘중에 하나보다 큰 경우에는 둘중에 작은것과 swap
        if not self.isLeaf(pos) and self.Heap[pos] > self.Heap[self.rchild[pos]] or self.Heap[pos] > self.Heap[self.lchild[pos]]:
            #왼쪽 오른쪽 둘중 작은것과 swap -> heapify
            if self.Heap[self.lchild[pos]] < self.Heap[self.rchild[pos]]:
                self.swap(pos, self.lchild[pos])
                self.minHeapify(self.lchild[pos])
            else:
                self.swap(pos, self.rchild[pos])
                self.minHeapify(self.rchild[pos])

    #insert
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))

    #Function to build minHeap
    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    #Remove and return min element
    def remove(self):
        removed = self.Heap[self.Front]
        self.Heap[self.Front] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.Front)
        return removed

    # Driver Code
    if __name__ == "__main__":
        print('The minHeap is ')
        minHeap = MinHeap(15)
        minHeap.insert(5)
        minHeap.insert(3)
        minHeap.insert(17)
        minHeap.insert(10)
        minHeap.insert(84)
        minHeap.insert(19)
        minHeap.insert(6)
        minHeap.insert(22)
        minHeap.insert(9)
        minHeap.minHeap()
        minHeap.Print()
        print("The Min val is " + str(minHeap.remove()))
