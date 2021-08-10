import sys, bisect
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

dp = [0] * N
sequence = [-sys.maxsize]
maxLength = 0
for i in range(N):
    if sequence[-1] < nums[i]:
        sequence.append(nums[i])
        dp[i] = len(sequence) - 1
        maxLength = dp[i]
    else:
        dp[i] = bisect.bisect_left(sequence, nums[i])
        sequence[dp[i]] = nums[i]
print(maxLength)
result = []
for i in range(N-1, -1, -1):
    if dp[i] == maxLength:
        result.append(nums[i])
        maxLength -= 1
print(*result[::-1])