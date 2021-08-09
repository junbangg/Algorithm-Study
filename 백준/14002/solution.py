import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
dp = [0] * N
sequence = [[n] for n in nums]
maxIndex = maxLength = -1
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            sequence[i] = sequence[j] + [nums[i]]
            dp[i] = dp[j]
    dp[i] += 1
    if maxLength < dp[i]:
        maxLength = dp[i]
        maxIndex = i
print(maxLength)
print(*sequence[maxIndex])