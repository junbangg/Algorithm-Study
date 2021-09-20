import sys
input = sys.stdin.readline


def validate(x, y):
    return 0 <= x < N and 0 <= y < M

def type_l(x, y):
    _max = -1
    if not validate(x, y):
        return _max
    # ㅣ
    ax, ay = x+1, y
    bx, by = x+2, y
    cx, cy = x+3, y
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy]
    # ㅡ
    ax, ay = x, y+1
    bx, by = x, y+2
    cx, cy = x, y+3
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    
    return _max

def type_square(x, y):
    _max = -1
    if not validate(x, y):
        return _max

    ax, ay = x + 1, y
    bx, by = x, y + 1
    cx, cy = x + 1, y + 1
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy]
    return _max


def type_L(x, y):
    _max = -1
    if not validate(x, y):
        return _max
    # L
    ax, ay = x + 1, y
    bx, by = x + 2, y
    cx, cy = x + 2, y + 1
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy]
    # L 반시계 방향 1
    ax, ay = x, y + 1
    bx, by = x, y + 2
    cx, cy = x - 1, y + 2
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    # L 반시계방향 2
    ax, ay = x, y + 1
    bx, by = x + 1, y + 1
    cx, cy = x + 2, y + 1
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    # L 반시계방향 3
    ax, ay = x+1 ,y
    bx, by = x, y + 1
    cx, cy = x, y + 2
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    # L 대칭
    ax, ay = x + 1, y
    bx, by = x + 2, y
    cx, cy = x + 2, y - 1
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    # L 대칭 시계방향 1
    ax, ay = x + 1, y
    bx, by = x + 1, y + 1
    cx, cy = x + 1, y + 2
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    # L 대칭 시계방향 2
    ax, ay = x, y + 1
    bx, by = x + 1, y
    cx, cy = x + 2, y
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    # L 대칭 시계방향 3
    ax, ay = x, y + 1
    bx, by = x, y + 2
    cx, cy = x + 1, y + 2
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    
    return _max

def type_s(x, y):
    _max = -1
    if not validate(x, y):
        return _max
    # 1
    ax, ay = x + 1, y
    bx, by = x + 1, y + 1
    cx, cy = x + 2, y + 1
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy]
    #2
    ax, ay = x , y + 1
    bx, by = x - 1, y + 1
    cx, cy = x - 1, y + 2
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    #3
    ax, ay = x + 1, y
    bx, by = x + 1, y - 1
    cx, cy = x + 2, y - 1
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    #4
    ax, ay = x, y + 1
    bx, by = x + 1, y + 1
    cx, cy = x + 1, y + 2
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    return _max

def type_fuckyou(x, y):
    _max = -1
    if not validate(x, y):
        return _max
    #1
    ax, ay = x, y + 1
    bx, by = x, y + 2
    cx, cy = x + 1, y + 1
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy]

    #2
    ax, ay = x + 1, y
    bx, by = x + 1, y - 1
    cx, cy = x + 1, y + 1
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])
    
    #3
    ax, ay = x + 1, y
    bx, by = x + 1, y + 1
    cx, cy = x + 2, y
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])

    #4
    ax, ay = x + 1, y
    bx, by = x + 1, y - 1
    cx, cy = x + 2, y
    if validate(ax, ay) and validate(bx, by) and validate(cx, cy):
        _max = max(_max, board[x][y] + board[ax][ay] + board[bx][by] + board[cx][cy])

    return _max

def getMax(x, y):
    return max(type_l(x, y), type_square(x, y), type_L(x, y), type_s(x, y), type_fuckyou(x, y))
    
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for x in range(N):
    for y in range(M):
        answer = max(answer, getMax(x, y))
print(answer)