import sys, copy
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N = int(input())
grid1 = [list(input())[:-1] for _ in range(N)]
grid2 = copy.deepcopy(grid1)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs1(x, y, color):
    if x < 0 or x >= N or y < 0 or y >= N or grid1[x][y] != color:
        return
    grid1[x][y] = 'X'
    for i in range(4):
        dfs1(x+dx[i], y+dy[i], color)

def dfs2(x,y,colors):
    if x < 0 or x >= N or y < 0 or y >= N or grid2[x][y] not in colors:
        return
    grid2[x][y] = 'X'
    for i in range(4):
        dfs2(x+dx[i], y+dy[i], colors)
# R / G / B
RGB = 0
for i in range(N):
    for j in range(N):
        if grid1[i][j] == 'R':
            dfs1(i,j,'R')
            RGB += 1
        if grid1[i][j] == 'G':
            dfs1(i, j,'G')
            RGB += 1
        if grid1[i][j] == 'B':
            dfs1(i, j, 'B')
            RGB += 1
print(RGB)
# RG / B
RG_B = 0
for i in range(N):
    for j in range(N):
        if grid2[i][j] == 'R' or grid2[i][j] == 'G':
            dfs2(i,j,['R', 'G'])
            RG_B += 1
        if grid2[i][j] == 'B':
            dfs2(i, j, ['B'])
            RG_B += 1
print(RG_B)
