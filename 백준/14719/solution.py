import sys
input = sys.stdin.readline
H, W = map(int, input().split())
nums = list(map(int, input().split()))

left, right, leftMax, rightMax = 0, W-1, nums[0], nums[-1]
answer = 0
while left <= right:
    leftMax, rightMax = max(nums[left], leftMax), max(nums[right], rightMax)
    if leftMax <= rightMax:
        answer += leftMax - nums[left]
        left += 1
    else:
        answer += rightMax - nums[right]
        right -= 1
print(answer)