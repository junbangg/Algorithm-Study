# Using Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        return min(count, key = count.get)
