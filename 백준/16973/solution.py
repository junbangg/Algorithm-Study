import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
H, W, SX, SY, FX, FY = map(int, input().split())
INF = sys.maxsize

def moveSquare(nx, ny, square):
    for i in range(len(square)):
        square[i][0] += nx
        square[i][1] += ny
    print(square)
    return square

def isValid(nx, ny, square):
    for x, y in square:
        if 0 > x + nx or N <= x + nx or 0 > y + ny or M <= y + ny or board[x + nx][y + ny] == 1:
            return False
    return True
    # for i in range(H):
    #     for j in range(W):
    #         nx, ny = x + i, y + j
    #         if 0 > nx or N <= nx or 0 > ny or M <= ny or board[nx][ny] == 1:
    #             return False
    # return True

def printBoard(board):
    for i in range(len(board)):
        print(*board[i])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(src_x, src_y, dest_x, dest_y, square):
    q = collections.deque()
    visited = [[INF] * M for _ in range(N)]
    visited[src_x][src_y] = 0
    q.append((src_x, src_y, square))
    while q:
        cur_x, cur_y, cur_square = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if isValid(dx[i], dy[i], cur_square) and visited[cur_x][cur_y] + 1 < visited[nx][ny]:
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                q.append((nx, ny, moveSquare(dx[i], dy[i], cur_square)))
    printBoard(visited)
    return visited[dest_x][dest_y]
# square 좌표들
square = []
# for i in range(H):
    # for j in range(W):
        # square.append([SX-1+i, SY-1+j])
for i in range(H):
    if i == 0 or i == H-1:
        for j in range(W):
            square.append([SX-1+i, SY-1+j])
    else:
        square.append([SX-1 + i, 0])
        square.append([SX-1 + i, W-1])
print(square)
print(bfs(SX-1, SY-1, FX-1, FY-1, square))