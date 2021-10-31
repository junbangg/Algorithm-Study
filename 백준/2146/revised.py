# 섬을 1~N 으로 Numbering 시킨다
# 색칠 안되는 곳들을 차례대로 BFS 시켜서 가장 짧은 다리 찾는다
#   - 이때, BFS를 하면서 다른 섬들을 찾아다닌다

import sys, collections
N = int(input())
board = [input().split() for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
edges = collections.defaultdict(set)

def markIslands(src_x, src_y, marker):
    visited = [[False] * N for _ in range(N)]
    visited[src_x][src_y] = True
    board[src_x][src_y] = marker
    q = collections.deque()
    q.append([src_x, src_y])
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if board[nx][ny] == '0':
                    edges[marker].add((cur_x, cur_y))
                else:
                    board[nx][ny] = marker
                    visited[nx][ny] = True
                    q.append([nx, ny])

# island 표시
visited = [[False] * N for _ in range(N)]
marker = 1
for x in range(N):
    for y in range(N):
        if board[x][y] == '1':
            markIslands(x,y,marker) 
            marker += 1

# 다리 탐색
def bfs(src_x, src_y, islandNum):
    visited = [[False] * N for _ in range(N)]
    visited[src_x][src_y] = True
    q = collections.deque()
    q.append([src_x, src_y, 0])
    while q:
        cur_x, cur_y, bridgeLength = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] != '0' and board[nx][ny] != islandNum:
                    return bridgeLength
                else:
                    q.append([nx, ny, bridgeLength + 1])

test = collections.defaultdict(list)
answer = float('inf')
for islandNum in edges:
    for x, y in edges[islandNum]:
        answer = min(answer, bfs(x, y, islandNum))
print(answer)

