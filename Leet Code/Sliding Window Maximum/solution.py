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

# Accepted Answer
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        result = []
        for index, value in enumerate(nums):
            # check if window is inside sliding window range
            # (index - k) = sliding window starting index
            if d and d[0] <= index - k:
                d.popleft()
            # Empty window until new value is at the front(if the new value is the max number)
            while d and nums[d[-1]] <= value:
                d.pop()
            d.append(index)
            # k-1 => sliding window last index
            if index >= k - 1:
                result.append(nums[d[0]])
        return result
