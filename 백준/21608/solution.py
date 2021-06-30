from collections import defaultdict
import sys
N = int(sys.stdin.readline())
grid = [[0 for _ in range(N)] for _ in range(N)]
fav = defaultdict(list)
for _ in range(N*N):
    inp = list(map(int, sys.stdin.readline().split()))
    fav[inp[0]] = inp[1:]

coords = defaultdict(tuple)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check1(friends):
    maxCount = -1
    cands = []
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 0:
                count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx >= 0 and nx < N and ny >= 0 and ny < N and grid[nx][ny] in friends:
                        count += 1
                if count >= maxCount:
                    if cands and cands[-1][0] < count:
                        cands.pop()
                    cands.append((count, x, y))
    return sorted(cands, key = lambda x: x[0])

def check(friend):
    cands = []
    x, y = coords[friend]
    # get candidate squares
    friendCount = -1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N and grid[nx][ny] == 0:
            cands.append((nx, ny))
    if not cands:
        return []
    cands2 = []
    maxCount = -1
    # get squares with most empty 
    for c in cands:
        x, y = c
        count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and grid[nx][ny] == 0:
                count += 1
        if maxCount <= count:
            maxCount = count
            cands2.append((count, x, y))
    return sorted(cands2, key = lambda x : (x[1], x[2]))
'''
for i, favPeople in fav.items():
    # start
    if not coords:
        coords[i] = (N//2, N//2)
        grid[N//2][N//2] = i
        continue
    # check rule 1
    check1(favPeople)
    cands = []
    for friend in favPeople:
        if friend in coords:
            temp = check(friend)
            if temp:
                cands.append(temp)
'''
