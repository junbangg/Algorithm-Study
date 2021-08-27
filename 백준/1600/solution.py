import sys, collections
input = sys.stdin.readline
K = int(input())
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

knightMoves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(src_x, src_y):
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    q = collections.deque()
    q.append((src_x, src_y, K, 0)) # x, y, k, moves
    while q:
        cur_x, cur_y, remaining_k, moves = q.popleft()
        # knight
        if remaining_k >= 1:
            for a, b in knightMoves:
                nx, ny = cur_x + a, cur_y + b
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                    if visited[nx][ny] == -1 or visited[nx][ny] < remaining_k - 1:
                        if nx == N-1 and ny == M-1:
                            return moves + 1
                        visited[nx][ny] = remaining_k - 1
                        q.append((nx, ny, remaining_k - 1, moves + 1))
        # 인접
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0<= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                if visited[nx][ny] == -1 or visited[nx][ny] < remaining_k:
                    if nx == N-1 and ny == M-1:
                        return moves + 1
                    visited[nx][ny] = remaining_k
                    q.append((nx, ny, remaining_k, moves + 1))
    return -1


if N == 1 and M == 1:
    print(0)
else:
    print(bfs(0, 0))