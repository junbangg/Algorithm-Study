import sys, collections, copy
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
H, W, SX, SY, FX, FY = map(int, input().split())
INF = sys.maxsize

def moveSquare(nx, ny, square):
    for i in range(len(square)):
        square[i][0] += nx
        square[i][1] += ny
    print('moved square')
    print(square)
    print('\n')
    return square

def isValid(nx, ny, square, visited):
    if visited[square[0][0] + nx][square[0][1] + ny] == 1:
        return False
    for x, y in square:
        if 0 > x + nx or N <= x + nx or 0 > y + ny or M <= y + ny or board[x + nx][y + ny] == 1:
            return False
    return True

def printBoard(board):
    for i in range(len(board)):
        print(*board[i])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(src_x, src_y, dest_x, dest_y, square):
    q = collections.deque()
    visited = [[0] * M for _ in range(N)]
    visited[src_x][src_y] = 1
    q.append((0, square))
    while q:
        print('popped from queue')
        print(q)
        cur_dist, cur_square = q.popleft()
        # cur_x, cur_y = cur_square[0][0], cur_square[0][1]
        for i in range(4):
            nx, ny = cur_square[0][0] + dx[i], cur_square[0][1] + dy[i]
            print(cur_square)
            if isValid(dx[i], dy[i], cur_square, visited):
                print(dx[i], dy[i], 'moving direction')
                print(nx, ny, 'valid coord\n')
                visited[nx][ny] = 1
                print('distance is', cur_dist+1)
                printBoard(visited)
                if nx == dest_x and ny == dest_y:
                    return cur_dist + 1
                q.append((cur_dist + 1, moveSquare(dx[i], dy[i], copy.deepcopy(cur_square))))
            else:
                print(dx[i], dy[i], 'moving direction')
                print(nx, ny, 'invalid coord\n')
                print('invalid')
                printBoard(visited)
    return -1
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
print(bfs(SX-1, SY-1, FX-1, FY-1, square))