import sys, copy
from itertools import combinations 
# input
N, M = map(int, input().split(' '))
ogMap = [list(map(int, input().split(' '))) for _ in range(N)]
viruses, candidates = [], []
# save 0 positions and 2(virus) positions
for i in range(N):
    for j in range(M):
        if ogMap[i][j] == 0:
            candidates.append((i, j))
        if ogMap[i][j] == 2:
            viruses.append((i, j))
# calculate all combinations
candidates = list(combinations(candidates, 3))
answer = -sys.maxsize
# N S W E
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# dfs
def dfs(x, y, map):
    for i in range(4):
        nextX, nextY = x + dx[i], y + dy[i]
        if nextX >= 0 and nextX < N and nextY >= 0 and nextY < M:
            if map[nextX][nextY] == 0:
                map[nextX][nextY] = 2
                dfs(x + dx[i], y + dy[i], map)

for cand in candidates:
    mapCopy = copy.deepcopy(ogMap)
    for x, y in cand:
        mapCopy[x][y] = 1
    for x, y in viruses:
        dfs(x, y, mapCopy)
    safeZone = sum(i.count(0) for i in mapCopy)
    answer = max(answer, safeZone)
print(answer)