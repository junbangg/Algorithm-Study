import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
q.append((0,0,1))
while q:
    cx, cy, count = q.popleft()
    if cx == N-1 and cy == M-1:
        print(count)
        break
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and not visited[nx][ny] and grid[nx][ny] == '1':
            visited[nx][ny] = True
            q.append((nx, ny, count + 1))

