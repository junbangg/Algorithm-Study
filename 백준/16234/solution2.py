import sys, collections
input = sys.stdin.readline
N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = collections.deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] != 0:
                continue
            if L <= abs(grid[cur_x][cur_y] - grid[nx][ny]) <= R:
                alliance.append((grid[nx][ny], nx, ny))
                visited[nx][ny] = 1
                q.append((nx, ny))

def apply(alliance):
    newVal = sum(list(map(lambda x: x[0], alliance))) // len(alliance)
    for _, x, y in alliance:
        grid[x][y] = newVal

answer = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    canMove = False
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                alliance = [(visited[x][y], x, y)]
                visited[x][y] = 1
                bfs(x, y)
                if len(alliance) > 1:
                    canMove = True
                    apply(alliance)
    if not canMove:
        break
    answer += 1
print(answer)