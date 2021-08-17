import sys, collections
input = sys.stdin.readline
N, M, R = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]

depth = min(N, M) // 2

# down, right 은 역순으로 배출(LIFO)
# left, up 는 들어온 순서대로 배출(FIFO)
for i in range(depth):
    for _ in range(R):
        left, up = collections.deque(), collections.deque()
        down, right = [], []
        for x in range(N):
            for y in range(M):
                # left
                if x == i and i < y < M-i:
                    left.append((grid[x][y], x, y))
                # down
                if i <= x < N-1-i and y == i:
                    down.append((grid[x][y], x, y))
                # right
                if x == N-1-i and i <= y < M-1-i:
                    right.append((grid[x][y], x, y))
                # up
                if i < x < N-i and y == M-1-i:
                    up.append((grid[x][y], x, y))
        #move
        while left:
            num, x, y = left.popleft()
            grid[x][y-1] = num
        while down:
            num, x, y = down.pop()
            grid[x+1][y] = num
        while right:
            num, x, y = right.pop()
            grid[x][y+1] = num
        while up:
            num, x, y = up.popleft()
            grid[x-1][y] = num
print(grid)
