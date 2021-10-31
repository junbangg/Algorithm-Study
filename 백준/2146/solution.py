# 섬을 1~N 으로 Numbering 시킨다
# 색칠 안되는 곳들을 차례대로 BFS 시켜서 가장 짧은 다리 찾는다
#   - 이때, BFS를 하면서 육지를 '

import sys, collections
sys.setrecursionlimit = 10**9
N = int(input())
board = [input().split() for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
edges = collections.defaultdict(set)
def markIslands(x, y, marker):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if board[nx][ny] == '0':
                edges[marker].add((x, y))
            else:
                visited[nx][ny] = True
                board[nx][ny] = marker
                markIslands(nx, ny, marker)

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
    # minBridge = float('inf')
    while q:
        cur_x, cur_y, bridge = q.popleft(0)
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            nxt_bridge = bridge
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] != '0' and board[nx][ny] != islandNum:
                    # minBridge = min(minBridge, nxt_bridge)
                    return nxt_bridge
                else:
                    nxt_bridge += 1
                    q.append([nx, ny, nxt_bridge])
    # return minBridge

test = collections.defaultdict(list)
answer = float('inf')
for islandNum in edges:
    for x, y in edges[islandNum]:
        answer = min(answer, bfs(x, y, islandNum))
print(answer)