import sys
N, M = list(map(int, sys.stdin.readline().split()))
r, c, d = list(map(int, sys.stdin.readline().split()))
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# N E S W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
def clean(x, y, d):
    global answer
    if map[x][y] == 0:
        answer += 1
        map[x][y] = 2
    count = 0
    while count < 4:
        dx, dy, dd = dir[d]
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < N and ny >= 0 and ny < M and map[nx][ny] == 0:
            clean(nx, ny, dd)
            return
        count += 1
        d = dd
    # 후진
    # 한바퀴 돌아서 d 가 다시 처음 d 가 됨
    dx, dy, dd = dir[d]
    nx, ny = x - dx, y - dy
    if nx < 0 or nx >= N or ny < 0 or ny >= M or map[nx][ny] == 1:
        return
    clean(nx, ny, d)
clean(r, c, d)
print(answer)