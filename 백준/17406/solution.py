import sys, itertools, copy
input = sys.stdin.readline

# 0. 연산 순서 설정
# 1. 회전 범위 계산 
# 2. 배열 회전
# 3. 최솟값 구하기


# 회전 함수
def rotate(x1, x2, y1, y2, arr):
    depth = min(x2+1-x1, y2+1-y1) // 2
    # up -> left -> down -> right
    for d in range(depth):
        cache = arr[x1 + d][y1 + d]
        # up
        for row in range(x1 + d + 1, x2 - d + 1):
            arr[row - 1][y1 + d] = arr[row][y1 + d]
        # left
        for col in range(y1 + d + 1, y2 - d + 1):
            arr[x2 - d][col-1] = arr[x2 - d][col]
        # down
        for row in range(x2 - d - 1, x1 + d - 1, -1):
            arr[row + 1][y2 - d] = arr[row][y2 - d]
        # right
        for col in range(y2 - d - 1, y1 + d - 1, - 1):
            arr[x1 + d][col + 1] = arr[x1 + d][col]
        # cache
        arr[x1 + d][y1 + d + 1] = cache

    return arr
    
# 입력
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmds = []
for _ in range(K):
    r, c, s = map(int, input().split())
    cmds.append((r-1, c-1, s))

# 최솟값 구하기
answer = float('inf')
for cmds in itertools.permutations(cmds, len(cmds)): # 가능한 연산 순열 설정
    arr_copy = copy.deepcopy(arr) # 배열 복사
    for cmd in cmds: 
        r, c, s = cmd
        arr_copy = rotate(r-s, r+s, c-s, c+s, arr_copy) # 배열 회전
    # 배열 값 최솟값 계산
    arr_val = float('inf')  
    for x in range(N):
        arr_val = min(arr_val, sum(arr_copy[x]))
    # 전체 최솟값 계산
    answer = min(answer, arr_val)

print(answer)