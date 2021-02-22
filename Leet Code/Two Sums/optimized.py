class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            search = target - v
            if search in nums[i+1:]:
                return [nums.index(v), nums[i+1:].index(search) + i+1]
