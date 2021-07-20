import sys, collections
input = sys.stdin.readline
R, C = map(int, input().split())
grid = []
dp = [[0]*C for _ in range(R)]
q = collections.deque()
found = False

dx = [1,-1,0,0]
dy = [0,0,1,-1]
start, dest = [], []

def bfs():
    while q:
        x, y, type = q.popleft()
        if type == 'D':
            print(dp[x][y])
            found = True
            break

        for i in range(4):
            nx, ny = x+dx[i], y + dy[i]
            #동일한 조건
            if 0<=nx<R and 0<=ny<C:
                if type == '*':
                    if grid[nx][ny] == '.' or grid[nx][ny] == 'S':
                        #체크인
                        grid[nx][ny] = '*'
                        q.append([nx, ny, '*'])
                else:
                    # [.] or [D]
                    if grid[nx][ny] == '.' or grid[nx][ny] == 'D':
                        if dp[nx][ny] == 0:
                            dp[nx][ny] = dp[x][y] + 1
                            q.append([nx,ny, grid[nx][ny]])


for i in range(R):
    row = list(input().strip())
    grid.append(row)
    for j in range(C):
        if row[j] == 'D':
            dest = [i, j]
        elif row[j] == 'S':
            start = [i, j, 'S']
        elif row[j] == '*':
            q.append([i, j, '*'])
q.append(start)
bfs()
if not found:
    print("KAKTUS")