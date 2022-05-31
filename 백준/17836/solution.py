import sys, collections
input = sys.stdin.readline
N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    sword = float('inf')
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    q = collections.deque()
    q.append((0, 0, 0)) #x, y, time
    while q:
        cur_x, cur_y, time = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and board[nx][ny] != 1:
                if nx == N-1 and ny == M-1:
                    return min(time + 1, sword)
                if board[nx][ny] == 2:
                    sword = abs(N-1-nx) + abs(M-1-ny) + time + 1
                visited[nx][ny] = 1
                q.append((nx, ny, time + 1))
    return float('inf')

answer = bfs()
print(answer if answer <= T else "Fail")

