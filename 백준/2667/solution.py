import sys
input = sys.stdin.readline

N = int(input())
grid = [list(input())[:-1] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global count
    if x < 0 or x >= N or y < 0 or y >= N or grid[x][y] == '0':
        return
    grid[x][y] = '0'
    count += 1 # add to house count
    for i in range(4):
        dfs(x + dx[i], y + dy[i])

houses = []
complexCount = count = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == '1':
            dfs(i, j)
            # complex
            complexCount += 1
            # house numbers
            houses.append(count)
            count = 0

print(complexCount)
for i in sorted(houses):
    print(i)
