import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [input().split() for _ in range(N)]

# for i in range(N, 0, -1):
    # print(i)
# 4 3 2 1

def rotate(arr):
    depth = min(N, M) // 2
    for d in range(depth):
        cache = arr[d][d]
        # top(left -> right)
        for j in range(d+1, M-d):
            arr[d][j-1] = arr[d][j]
        # right (bottom -> top)
        for i in range(1+d, N-d):
            arr[i-1][M-1-d] = arr[i][M-1-d]
        # bottom (right -> left)
        for j in range(M-2-d, d-1, -1):
            arr[N-1-d][j+d] = arr[N-1-d][j-1+d]
        # left (bottom -> top)
        for i in range(N-2-d, d-1, -1):
            arr[i+d][d] = arr[i][d]
        arr[d+1][d] = cache
    print(arr)
    return arr

print(rotate(arr))
        