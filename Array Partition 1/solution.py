# My answer O(n)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        while nums:
            answer += min(nums.pop(), nums.pop())
        return answer

# Book - 1
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        temp = []
        for i in nums:
            temp.append(i)
            if len(temp) == 2:
                answer += min(temp)
                temp = []

        return answer

# Book - 2
def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        for i,v in enumerate(nums):
            if i % 2 == 0:
                answer += v
        return answer
# Book -2 my version
def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        temp = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        return sum(temp)
# or
def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return functools.reduce(lambda a, b: a+b, [v for i,v in enumerate(nums) if i%2==0])

# or

def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
