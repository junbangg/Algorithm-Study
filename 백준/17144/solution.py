import sys
input = sys.stdin.readline

#먼지 확산
def spread(dust):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    update = []
    for x, y in dust:
        counter = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                counter += 1
                update.append((nx, ny, board[x][y] // 5)) # 확산 할 먼지 좌표와 수치 저장
        board[x][y] -= board[x][y] // 5 * counter # 기존 좌표에 먼지 수치 변화
    # 알맞는 좌표에 먼지 수치 더하기
    for x, y, amount in update:
        board[x][y] += amount

def purify(upper, lower):
    # upper
    # left -> up -> right -> down
    cache = board[0][0]
    # left
    for col in range(1, C):
        board[0][col-1] = board[0][col]
    # up
    for row in range(1, upper+1):
        board[row-1][C-1] = board[row][C-1]
    # right
    for col in range(C-1, 1, -1):
        board[upper][col] = board[upper][col-1]    
    # down
    for row in range(upper-1, 0, -1):
        board[row][0] = board[row-1][0]

    board[1][0] = cache
    board[up][1] = 0 # 공기청정기에서 나오는 깨끗한 공기(0)

    # lower
    # up -> left -> down -> right
    
    # up
    for row in range(lower + 2, R):
        board[row-1][0] = board[row][0]
    # left
    for col in range(1, C):
        board[R-1][col-1] = board[R-1][col]
    # down
    for row in range(R-1, lower-1, -1):
        board[row][C-1] = board[row-1][C-1]
    # right
    for col in range(C-1, 1, -1):
        board[lower][col] = board[lower][col-1]

    board[lower][1] = 0 # 공기청정기에서 나오는 깨끗한 공기(0)
    

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
# main 
for _ in range(T):
    machine = []
    # 1. 미세먼지 확산
    dust = []
    for x in range(R):
        for y in range(C):
            if board[x][y] == -1: # 공기청정기 x 좌표 기록
                machine.append(x)
            elif board[x][y] > 0: # 먼지 좌표 기록
                dust.append((x, y))
    spread(dust) # 먼지 확산

    # 2. 공기청정기 작동
    up, low = sorted(machine)
    purify(up, low)

# 먼지 계산
total = 0
for x in range(R):
    total += sum(board[x])
print(total + 2)
