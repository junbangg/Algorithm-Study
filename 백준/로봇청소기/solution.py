import sys
N, M = list(map(int, sys.stdin.readline().split()))
r, c, d = list(map(int, sys.stdin.readline().split()))
direction = {0: 0,
             1: 3,
             3: 1}
d = direction[d]
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
'''
dir = { 0 : (0, -1), #N
        1: (-1, 0), #E
        2: (0, 1), #S
        3: (1, 0) } #W
'''
dir = { 0 : (0, -1, 1), #N
        1 : (1, 0, 2), #W
        2 : (0, 1, 3), #S
        3 : (-1, 0, 0) }#E
answer = 0
def clean(x, y, d):
    global answer
    if map[x][y] == 0:
        answer += 1
        map[x][y] = -1
    count = 0
    while count < 4:
        dx, dy, dd = dir[d]
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < N and ny >= 0 and ny < M and map[nx][ny] < 1:
            clean(nx, ny, dd)
        count += 1
        d = dd
    return
clean(r, c, d)
print(answer)
'''        
5 5 
2 3 0
1 1 0 1 1
1 0 0 0 1
1 0 0 0 1
1 0 1 1 1
1 0 0 0 1
'''

