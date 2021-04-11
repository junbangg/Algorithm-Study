# Brute force 
class Solution:
    def rob(self, nums: List[int]) -> int:
        def recurse(i):
            if i < 0:
                return 0
            return max(recurse(i-1), recurse(i-2) + nums[i])
        return recurse(len(nums)-1)

# Memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp.popitem()[1]
