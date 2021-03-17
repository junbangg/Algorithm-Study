# first approach (pythonic solution) doesn't work
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return ''.join(sorted(map(str, nums), reverse = True))

# second approach
class Solution:
    def compare(self, a, b):
        temp_a, temp_b = a, b
        # b 길이가 a 길이보다 클 때
        while len(temp_a) < len(temp_b):
            temp_a += temp_a[-1]
        # a 길이가 b 길이 보다 클 때
        while len(temp_b) < len(temp_a):
            temp_b += temp_b[-1]
        # a길이가 b길이랑 같을 때
        # return a if temp_a > temp_b else b
        return temp_a < temp_b

    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), reverse = True)
        #nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(i, 0, -1):
                if self.compare(nums[j-1], nums[j]):
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return ''.join(nums)

# Third Approach
class Solution:
    def compare(self, a, b):
        return a + b < b + a

    def largestNumber(self, nums: List[int]) -> str:
        # edge case
        if set(nums) == {0}:
            return "0"
        nums = sorted(map(str, nums), reverse = True)
        #nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(i, 0, -1):
                if self.compare(nums[j-1], nums[j]):
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return ''.join(nums)

# Third Approach trimmed down
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # edge case
        if set(nums) == {0}:
            return "0"
        nums = sorted(map(str, nums), reverse = True)
        for i in range(len(nums)):
            for j in range(i, 0, -1):
                if nums[j-1] + nums[j] < nums[j] + nums[j-1]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return ''.join(nums)


