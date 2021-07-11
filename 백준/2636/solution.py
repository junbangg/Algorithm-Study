from collections import deque
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    global count
    q = deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and visited[nx][ny] == 0:
                if grid[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif grid[nx][ny] == 1:
                    count += 1
                    visited[nx][ny] = 1
                    grid[nx][ny] = 0

prev, time = 0, 0
while True:
    count = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    bfs(0, 0)
    if count == 0:
        break
    prev = count
    time += 1

print(time)
print(prev)