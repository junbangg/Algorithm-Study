import sys
input = sys.stdin.readline
N, M = map(int, input().split())
apps = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
maxCost = sum(costs)
dp = [[0 for _ in range(maxCost+1)] for _ in range(len(costs))]
result = maxCost
for i in range(1, len(costs)):
    for j in range(maxCost+1):
        if costs[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i]] + apps[i])
        if dp[i][j] >= M:
            result = min(result, j)
print(result)