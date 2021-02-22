class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            search = target - v
            if search in nums[i+1:]:
                return [nums.index(v), nums[i+1:].index(search) + i+1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for key, val in enumerate(nums):
            if target - val in dic and dic[target-val] != key:
                return [key, dic[target - val]]
            dic[val] = key
