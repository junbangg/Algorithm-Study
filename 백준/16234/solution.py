import sys
sys.setrecursionlimit(10**5)
N, L, R = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]
dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x,y):
    global alliance, members
    for i in range(4):
        nx, ny = x+dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] != 0:
            continue
        if L <= abs(grid[x][y] - grid[nx][ny]) <= R:
            members += 1
            alliance.append((nx, ny))
            visited[nx][ny] = 1
            dfs(nx, ny)

def apply(A, num):
    total = 0
    for x, y in A:
        total += grid[x][y]
    newNum = total // num
    for x, y in A:
        grid[x][y] = newNum

answer = 0
while True:
    canMove = False
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                members = 1
                alliance = [(i, j)]
                visited[i][j] = 1
                dfs(i,j)
                if members > 1:
                    canMove = True
                    apply(alliance, members)
    if not canMove:
        break
    answer += 1
print(answer)