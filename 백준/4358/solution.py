import sys
# Fenwick Tree
class Fenwick(list):
    # 펜윅트리 생성
    def __init__(self, nums):
        #index 1 부터 넣는다
        self.prefix = [0] * (len(nums)+1)
        self.nums = nums
        self.n = len(nums)
        for i in range(len(nums)):
            self.add(i+1, nums[i])
    
    def add(self, x, val):
        while x <= self.n:
            self.prefix[x] += val
            x+= self.lowbit(x)
    
    def lowbit(self, x):
        return x & -x
    
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.prefix[x]
            x -= self.lowbit(x)
        return res

    def update(self, i, val):
        self.add(i+1, val-self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        if not self.nums: return 0
        if i>j: return self.sum(i+1) - self.sum(j)
        return self.sum(j+1) - self.sum(i)



input = sys.stdin.readline
N, Q = map(int, input().split())
temp = list(map(int, input().split()))
temp.insert(0, 0)
nums = Fenwick(temp)

for _ in range(Q):
    x,y,a,b = map(int, input().split())
    print(nums.sumRange(x, y))
    nums.update(a, b)