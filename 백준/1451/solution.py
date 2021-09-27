import sys
input = sys.stdin.readline
N, M = map(int, input().split())
rect = [[0] * (M+1)]
for _ in range(N):
    rect.append([0] + list(map(int, list(input().rstrip()))))

prefix = [[0 for _ in range(M+1)] for _ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, M+1):
        prefix[x][y] = prefix[x-1][y] + prefix[x][y-1] - prefix[x-1][y-1] + rect[x][y]


def getSum(x1, y1, x2, y2):
    return prefix[x2][y2] - prefix[x2][y1 - 1] - prefix[x1 - 1][y2] + prefix[x1 - 1][y1 - 1]


def _print(prefix):
    for x in range(len(prefix)):
        print(*prefix[x])
_print(prefix)

answer = 0
# 가로 분리
for i in range(1, N-1):
    for j in range(i+1, N):
        r1 = getSum(1, 1, i, M)
        r2 = getSum(i+1, 1, j, M)
        r3 = getSum(j+1, 1, N, M)
        answer = max(answer, r1 * r2 * r3)
# 세로분리
for i in range(1, M-1):
    for j in range(i+1, M):
        r1 = getSum(1, 1, N, i)
        r2 = getSum(1, i+1, N, j)
        r3 = getSum(1, j+1, N, M)
        answer = max(answer, r1 * r2 * r3)

# type 3
for i in range(1, M):
    for j in range(1, N):
        r1 = getSum(1, 1, N, i)
        r2 = getSum(1, i+1, j, M)
        r3 = getSum(j+1, i+1, N, M)
        answer = max(answer, r1 * r2 * r3)

#type 4
for i in range(1, N):
    for j in range(1, M):
        r1 = getSum(1, 1, i, j)
        r2 = getSum(i+1, 1, N, j)
        r3 = getSum(1, j+1, N, M)
        answer = max(answer, r1 * r2 * r3)

# type 5
for i in range(1, N):
    for j in range(1, M):
        r1 = getSum(1, 1, i, M)
        r2 = getSum(i+1, 1, N, j)
        r3 = getSum(i+1, j+1, N, M)
        answer = max(answer, r1 * r2 * r3)

# type 6
for i in range(1, N):
    for j in range(1, M):
        r1 = getSum(1, 1, i, j)
        r2 = getSum(1, j+1, i, M)
        r3 = getSum(i+1, 1, N, M)
        answer = max(answer, r1 * r2 * r3)

print(answer)