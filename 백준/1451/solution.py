import sys
input = sys.stdin.readline
N, M = map(int, input().split())
rect = [[0] + list(map(int, list(input().rstrip()))) for _ in range(N)]
print(rect)
answer = 0
prefix = [[0 for _ in range(M+1)] for _ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, M+1):
        prefix[x][y] = prefix[x-1][y] + prefix[x][y-1] - prefix[x-1][y-1] + rect[x][y]


print(prefix)