import sys, collections
input = sys.stdin.readline
N, M, R = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]

depth = min(N, M) // 2
# down, right 은 역순으로 이동
# left, up 는 순서대로 이동
for i in range(depth):
    for _ in range(R):
        # left -> up -> right -> down 순서대로 이동하면 [i][i] 만 캐싱 하면 된다
        cache = grid[i][i]
        #left
        for col in range(i+1, M-i):
            grid[i][col-1] = grid[i][col]
        # up
        for row in range(i+1, N-i):
            grid[row-1][M-1-i] = grid[row][M-1-i]
        # right
        for col in range(M-2-i, i-1, -1):
            grid[N-1-i][col+1] = grid[N-1-i][col]
        # down
        for row in range(N-2-i, i-1, -1):
            grid[row+1][i] = grid[row][i]
        
        grid[i+1][i] = cache

for i in range(N):
    print(*grid[i])