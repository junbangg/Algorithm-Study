# Brute Force
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, k
        maxwindow = []
        while right <= len(nums):
            window = nums[left:right]
            maxwindow.append(max(window))
            left += 1
            right += 1
        return maxwindow
# or 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        answer = []
        for i in range(len(nums) - k + 1):
            answer.append(max(nums[i:i+k]))
        return answer

# Optimized
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        answer = []
        windowmax = float('inf')
        for index, value in enumerate(nums):
            window.append(value)
            if index < k - 1:
                continue
            
            if windowmax == float('inf'):
                windowmax = max(window)
            elif value > windowmax:
                windowmax = value
            answer.append(windowmax)
            
            if windowmax == window.popleft():
                windowmax = float('inf')
        return answer
