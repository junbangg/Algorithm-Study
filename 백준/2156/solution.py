import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 10000
for i in range(N):
    arr[i] = int(input())

dp = [0] * 10000
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(dp[1], arr[0] + arr[2], arr[2] + arr[1])

for i in range(3, N):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
    dp[i] = max(dp[i-1], dp[i])

print(dp[N-1])
