import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
H, W, SX, SY, FX, FY = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def isValid(nx, ny, visited):
    # 기본 bfs 범위 확인
    if 0 > nx or N <= nx or 0 > ny or M <= ny or visited[nx][ny]:
        return False
    # 직사각형 범위가 맵 밖으로 나가는지 확인
    if nx + H - 1 >= N or ny + W - 1 >= M:
        return False
    # 직사각형 범위 안에 벽이 있는지 확인
    for x, y in walls:
        if nx <= x < nx + H and ny <= y < ny + W:
            return False
    return True

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

walls = []
for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            walls.append((x, y))
print(bfs(SX-1, SY-1, FX-1, FY-1))