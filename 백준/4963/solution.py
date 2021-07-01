import sys
sys.setrecursionlimit(3000)
input = sys.stdin.readline

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]
grid = []
def dfs(x, y):
    global M
    global N
    if x < 0 or x >= N or y < 0 or y >= M or grid[x][y] == 0:
        return
    grid[x][y] = 0
    for i in range(8):
        dfs(x + dx[i], y + dy[i])

while 1:
    count = 0
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        exit(0)
    grid = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)



