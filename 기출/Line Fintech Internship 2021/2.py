from collections import deque
from math import ceil, sqrt

def getDistance(x1, x2, y1, y2):
    return sqrt((y1-x1)**2 + (y2-x2)**2)

def bfs(_map, N, M, src_x, src_y):
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    q = deque([])
    q.append([src_x, src_y])
    visited = [[False] * M for _ in range(N)]
    visited[src_x][src_y] = True
    longest = -float('inf')
    lastIsland_x, lastIsland_y = src_x, src_y
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if _map[nx][ny] == 1:
                    # print(cur_x, cur_y)
                    # print(nx, ny)
                    islandDistance = getDistance(lastIsland_x, lastIsland_y, nx, ny)
                    # print(nxt_dist)
                    lastIsland_x, lastIsland_y = nx, ny
                    longest = max(longest, islandDistance)
                visited[nx][ny] = True
                q.append([nx, ny])
    return longest

def solution(x, y):
    coords = list(zip(x, y))
    # create Map
    N = M = 0
    for x, y in coords:
        N = max(N, x)
        M = max(M, y)
    N += 1
    M +=1
    _map = [[0] * M for _ in range(N)]
    for x, y in coords:
        _map[x][y] = 1
    answer = bfs(_map, N, M, coords[0][0], coords[0][1])
    return int(ceil(answer))

x = [1, 2, 6, 8]
y = [1, 2, 5, 7]
print(solution(x, y))
    

    
# import math, itertools

# def getDistance(x1, x2, y1, y2):
#     return math.sqrt((y1-x1)**2 + (y2-x2)**2)

# def solution(x, y):
#     coords = list(zip(x, y))
#     perms = itertools.permutations(coords, len(coords))
#     answer = -float('inf')
#     for perm in perms:
#         for i in range(1, len(perm)):
#             cur_x, cur_y = perm[i-1]
#             nxt_x, nxt_y = perm[i]
#             answer = max(answer, getDistance(cur_x, cur_y, nxt_x, nxt_y))
#     return math.ceil(answer)


# x = [1, 2, 6, 8]
# y = [1, 2, 5, 7]
# print(solution(x, y))