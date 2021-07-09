N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N
maxNum = 0
for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
