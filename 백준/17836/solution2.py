import sys, collections
input = sys.stdin.readline
N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def getTime(x, y, nx, ny):
    return abs(nx - x) + abs(ny - y)

def bfs():
    swordTime = float('inf')
    time = [[float('inf') for _ in range(M)] for _ in range(N)]
    q = collections.deque()
    time[0][0] = 0
    q.append([0, 0])
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 > nx or nx >= N or 0 > ny or ny >= M or board[nx][ny] == 1:
                continue
            nextTime = time[x][y] + 1

            if time[nx][ny] >= nextTime:
                time[nx][ny] = nextTime
                q.append([nx, ny])
            if board[nx][ny] == 2:
                nextTime += getTime(nx, ny, N-1, M-1)
                sword = nextTime
            if nx == N-1 and ny == M-1:
                return min(time[N-1][M-1], sword)

    return  
print(bfs())
