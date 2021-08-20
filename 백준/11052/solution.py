import sys
input = sys.stdin.readline
N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = cards[1]
dp[2] = max(cards[2], cards[1] * 2)
for i in range(3, N+1):
    dp[i] = cards[i]
    # 약수들
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp[N])
