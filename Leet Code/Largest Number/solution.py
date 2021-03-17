# first approach (pythonic solution) doesn't work
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return ''.join(sorted(map(str, nums), reverse = True))
