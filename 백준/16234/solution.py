import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N, L, R = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(cur_x,cur_y):
    for i in range(4):
        nx, ny = cur_x + dx[i], cur_y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] != 0:
            continue
        if L <= abs(grid[cur_x][cur_y] - grid[nx][ny]) <= R:
            alliance.append((grid[nx][ny], nx, ny))
            visited[nx][ny] = 1
            dfs(nx, ny)

def apply(alliance):
    newVal = sum(list(map(lambda x: x[0], alliance))) // len(alliance)
    for _, x, y in alliance:
        grid[x][y] = newVal


answer = 0
while True:
    canMove = False
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                alliance = [(grid[i][j], i, j)]
                visited[i][j] = 1
                dfs(i,j)
                if len(alliance) > 1:
                    canMove = True
                    apply(alliance)
    if not canMove:
        break
    answer += 1
print(answer)