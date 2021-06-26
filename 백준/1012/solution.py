import sys
sys.setrecursionlimit(10**6)

tc = int(sys.stdin.readline())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, n, m):
    global grid
    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
        return
    grid[x][y] = 0
    for i in range(4):
        dfs(x + dx[i], y + dy[i], n, m)
    return

for _ in range(tc):
    M, N, K = map(int, sys.stdin.readline().split())
    #map
    grid = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        grid[x][y] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                dfs(i, j, N, M)
                count += 1
    print(count)


