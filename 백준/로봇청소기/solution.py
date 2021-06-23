import sys
N, M = list(map(int, sys.stdin.readline().split()))
r, c, d = list(map(int, sys.stdin.readline().split()))
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#N E S W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
def clean(x, y, d):
    global answer
    if map[x][y] == 0:
        answer += 1
        map[x][y] = 2
    for _ in range(4):
        left = (d - 1) % 4
        nx, ny = x + dx[left], y + dy[left]
        if map[nx][ny] == 0:
            clean(nx, ny, left)
            return
        d = left
    # 후진
    # 한바퀴 돌아서 d 가 다시 처음 d 가 됨
    nx, ny = x - dx[d], y - dy[d]
    if map[nx][ny] == 1:
        return
    clean(nx, ny, d)
clean(r, c, d)
print(answer)
