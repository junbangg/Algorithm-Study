import sys, collections
input = sys.stdin.readline
board = [list(input().rstrip()) for _ in range(8)]
dest = (0, 7)
kings, walls = collections.deque([(7, 0)]), collections.deque()

def printBoard():
    for i in range(8):
        print(*board[i])
    print('\n')
#     0, E, W, N, S, NE, NW, SE, SW
dx = [0, 0, 0, -1, 1, -1, -1, 1, 1]
dy = [0, 1, -1, 0, 0, 1, -1, 1, -1]
def bfs():
    while kings:
        nxt_kings, pre_walls, nxt_walls = [], [], []
        visited = [[0 for _ in range(8)] for _ in range(8)]

        while walls:
            cur_x, cur_y = walls.popleft()
            pre_walls.append((cur_x, cur_y))
            if cur_x + 1 < 8:
                board[cur_x+1][cur_y] = '#'
                nxt_walls.append((cur_x+1, cur_y))

        while kings:
            cur_x, cur_y = kings.popleft()
            if cur_x == 0 and cur_y == 7 :
                return 1
            if board[cur_x][cur_y] == '#':
                continue
            for i in range(9):
                nx, ny = cur_x + dx[i], cur_y + dy[i]
                if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    nxt_kings.append((nx, ny))

        # move walls 
        for x, y in pre_walls:
            board[x][y] = '.'
        for x, y in nxt_walls:
            walls.append((x, y))
        # move King
        for x, y in nxt_kings:
            kings.append((x, y))
        
        printBoard()

    return 0



for x in range(8):
    for y in range(8):
        if board[x][y] == '#':
            walls.append((x, y))
printBoard()
print(bfs())