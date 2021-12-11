import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

depth = min(N, M) // 2
for _ in range(R):
    for d in range(depth):
        cache = arr[d][d]
        # top(left -> right)
        for col in range(1+d, M-d):
            arr[d][col-1] = arr[d][col]
        # right (bottom -> top)
        for row in range(1+d, N-d):
            arr[row-1][M-1-d] = arr[row][M-1-d]
        # bottom (right -> left)
        for col in range(M-1-d, d, -1):
            arr[N-1-d][col] = arr[N-1-d][col-1]
        # left (bottom -> top)
        for row in range(N-1-d, 1+d, -1):
            arr[row][d] = arr[row-1][d]
        arr[d+1][d] = cache

for i in range(len(arr)):
    print(*arr[i])
        