import sys
class Fenwick(object):
    def __init__(self, nums):
        # 펜윅트리 생성 
        # index 1부터.. 앞에 0을 넣어준 리스트로 만든다
        self.sum_array = [0] * (len(nums) + 1)
        self.nums = nums
        self.n = len(nums)
        for i in range(len(nums)):
            self.add(i + 1,nums[i])


    def add(self,x,val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)


    def lowbit(self,x):
        return x & -x

    def sum(self,x):
        res = 0
        while x >0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res

    def update(self, i, val):
        # i 인덱스에 val 을 넣는다
        self.add(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        # 구간합
        # i~j 까지의 구간합 리턴
        if not self.nums: return  0
        return self.sum(j+1) - self.sum(i)

input = sys.stdin.readline
N, M, K = map(int, input().split())
temp= list(int(input()) for _ in range(N))
temp.insert(0, 0)
nums = Fenwick(temp)

cmds = []
for _ in range(M+K):
    a,b,c = map(int, input().split())
    cmds.append((a,b,c))

for a,b,c in cmds:
    if a == 1:
        # b index 를 c 로
        nums.update(b, c)
    else:
        print(nums.sumRange(b, c))
    