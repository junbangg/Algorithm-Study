# Dynamic Programming
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if num not in counts:
                counts[num] = nums.count(num)
            if counts[num] > len(nums) // 2:
                return num

# Divide and Conquer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        a = self.majorityElement(nums[mid:])
        b = self.majorityElement(nums[:mid])
        return [b, a][nums.count(a) > mid]

# Pythonic
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

# Hash Map
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key = counts.get)

# Boyer-Moore Voting algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
