import sys, collections
input = sys.stdin.readline
R, C = map(int, input().split())
grid = []
visited = [[0]*C for _ in range(R)]
water = collections.deque()
q = collections.deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]
dest = []

def bfs():
    while water or q:
        dTemp, wTemp = [], []
        while q:
            x, y = q.popleft()
            if grid[x][y] != '*':
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0<=nx<R and 0<=ny<C and visited[nx][ny] == 0 and grid[nx][ny] != 'X' and grid[nx][ny] != '*':
                        grid[nx][ny] = grid[x][y] + 1
                        visited[nx][ny] = True
                        dTemp.append([nx,ny])
        while water:
            x, y = water.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx == dest[0] and ny == dest[1]:
                    continue
                if 0<=nx<R and 0<=ny<C and grid[nx][ny] != '*' and grid[nx][ny] != 'X':
                    grid[nx][ny] = '*'
                    wTemp.append([nx,ny])
        for d in dTemp:
            q.append(d)
        for w in wTemp:
            water.append(w)

for i in range(R):
    row = list(input().strip())
    grid.append(row)
    for j in range(C):
        if row[j] == 'D':
            dest = [i, j]
        elif row[j] == 'S':
            q.append([i, j])
            visited[i][j] = True
            grid[i][j] = 0
        elif row[j] == '*':
            water.append([i, j])

bfs()
result = grid[dest[0]][dest[1]]
if result != 'D':
    print(result)
else:
    print("KAKTUS")