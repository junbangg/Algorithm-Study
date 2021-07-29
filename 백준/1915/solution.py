import sys, copy
input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

maxEdge = 0
for x in range(1, N+1):
    for y in range(1, M+1):
        if grid[x-1][y-1] == 1:
            dp[x][y] = min(dp[x-1][y-1], dp[x][y-1], dp[x-1][y]) + 1
            maxEdge = max(dp[x][y], maxEdge)
print(maxEdge**2)