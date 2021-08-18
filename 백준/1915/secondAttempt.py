import sys
input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(N)]
maxSize = 0 
for x in range(N):
    for y in range(M):
        if 0<x and 0<y and grid[x][y] == 1:
            grid[x][y] += min(grid[x-1][y-1], grid[x-1][y], grid[x][y-1])
        maxSize = max(grid[x][y], maxSize)
print(maxSize**2)