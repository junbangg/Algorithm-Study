# Two Pointer Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        answer = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            if left_max <= right_max:
                answer += left_max - height[left]
                left += 1
            else:
                answer += right_max - height[right]
                right -= 1
        return answer

# Stack Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                water = min(height[i], height[stack[-1]]) - height[top]
                answer += water * distance
            stack.append(i)
        return answer
