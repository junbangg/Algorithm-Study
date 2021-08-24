import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(src_x, src_y):
    global count
    q = collections.deque()
    q.append((src_x, src_y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                # 치즈
                if grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    count += 1
                # 새로운 공기
                else:
                    q.append((nx, ny))

prev = time = 0
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