import sys
input = sys.stdin.readline

N = int(input())
nums = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
for i in range(1, N+1):
    nums[i] = int(input())
dp[0] = nums[0]
dp[1] = nums[0] + nums[1]
dp[2] = max(nums[1] + nums[2], nums[0] + nums[2])
for i in range(3, N+1):
    dp[i] = max(dp[i - 3] + nums[i - 1] + nums[i], dp[i - 2] + nums[i])
    # dp[i] = max(dp[i-2] + nums[i], nums[i-1] + nums[i])
print(dp[N])