import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(src_x, src_y):
    visited = [[False] * M for _ in range(N)]
    visited[src_x][src_y] = True
    q = collections.deque()
    q.append([src_x, src_y, 1])
    while q:
        cur_x, cur_y, dist = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] != 0:
                visited[nx][ny] = True
                result[nx][ny] = dist
                q.append((nx, ny, dist + 1))

for x in range(N):
    for y in range(M):
        if board[x][y] == 2:
            bfs(x, y)
            break
        
for x in range(N):
    for y in range(M):
        if result[x][y] == 0 and board[x][y] == 1:
            result[x][y] = -1

for i in range(N):
    print(*result[i])



