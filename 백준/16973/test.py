import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
H, W, SX, SY, FX, FY = map(int, input().split())

def isValid(nx, ny, visited):
    if visited[nx][ny]:
        return False
    # square
    for i in range(H):
        for j in range(W):
            sq_x = nx + i
            sq_y = ny + j
            if 0 > sq_x or N <= sq_x or 0 > sq_y or M <= sq_y or board[sq_x][sq_y] == 1:
                return False
    return True

def printBoard(board):
    for i in range(len(board)):
        print(*board[i])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(src_x, src_y, dest_x, dest_y):
    q = collections.deque()
    visited = [[0] * M for _ in range(N)]
    visited[src_x][src_y] = 1
    q.append((0, src_x, src_y)) # time, x, y
    while q:
        time, cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if isValid(nx ,ny, visited):
                if nx == dest_x and ny == dest_y:
                    return time + 1
                visited[nx][ny] = 1
                q.append((time+1, nx, ny))
    return -1
print(bfs(SX-1, SY-1, FX-1, FY-1))