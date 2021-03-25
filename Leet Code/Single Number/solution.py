# Using Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        return min(count, key = count.get)

# Bit Manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in nums:
            single ^= i
        return single

