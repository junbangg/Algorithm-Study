class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        l, r = 1, 1
        for i in range(len(nums)):
            left.append(l)
            l *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            left[i] *= r
            r *= nums[i]
        return left
