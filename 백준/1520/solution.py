import sys

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and grid[x][y] > grid[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))
