# 3칸"씩" 이동해야됨;
import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())
_map = [input().split() for _ in range(N)]
src = list(map(int, input().split()))
dest = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def getMinDirectionCommand(before, after):
    if abs(before-after) == 3:
        return 1
    else:
        return abs(before-after)

def printBoard(board):
    for i in range(len(board)):
        print(*board[i])

def bfs(src_x, src_y, src_dir, dest_x, dest_y, dest_dir): # 전부 1 뺴기
    visited = [[float('inf')] * M for _ in range(N)]
    visited[src_x][src_y] = 0
    q = []
    heapq.heappush(q, [0, src_x, src_y, src_dir, 0])
    while q:
        cur_cost, cur_x, cur_y, cur_dir, cur_leap = heapq.heappop(q)
        for nxt_dir in range(4):
            nx, ny = cur_x + dx[nxt_dir], cur_y + dy[nxt_dir]
            if 0 <= nx < N and 0 <= ny < M and _map[nx][ny] == '0':
                minDirectionCommands = getMinDirectionCommand(cur_dir, nxt_dir)
                nxt_cost = cur_cost + minDirectionCommands
                nxt_leap = cur_leap
                if minDirectionCommands > 0:
                    nxt_cost += 1
                    nxt_leap = 0
                else:
                    if nxt_leap == 0:
                        nxt_cost += 1
                nxt_leap += 1
                if nxt_leap == 3:
                    nxt_leap = 0
                # if nx == dest_x and ny == dest_y:
                    # print("도착스: nx, ny, 방향 적용 전, 방향 적용 후", cur_x, cur_y, nxt_cost, nxt_cost + getMinDirectionCommand(nxt_dir, dest_dir))
                if nxt_cost < visited[nx][ny]:
                    visited[nx][ny] = nxt_cost
                    if nx == dest_x and ny == dest_y:
                        visited[nx][ny] += getMinDirectionCommand(nxt_dir, dest_dir)
                    heapq.heappush(q, (nxt_cost, nx, ny, nxt_dir, nxt_leap))
    return visited[dest_x][dest_y]

def convertDirection(num):
    if num == 1:
        return 1
    if num == 2:
        return 3
    if num == 3:
        return 2
    if num == 4:
        return 0

print(bfs(src[0]-1, src[1]-1, src[2]-1, dest[0]-1, dest[1]-1, convertDirection(dest[2])))

# 5 6
# 0 0 0 0 0 0
# 0 1 1 0 1 0
# 0 1 0 0 0 0
# 0 0 1 1 1 0
# 1 0 0 0 0 0
# 4 2 3
# 3 5 1

# 5 6
# 0 0 0 0 0 0
# 0 1 1 0 1 0
# 0 1 0 0 0 0
# 0 0 1 1 1 0
# 1 0 0 0 0 0
# 4 2 3
# 1 6 3

# 5 6
# 0 0 0 0 0 0
# 0 1 1 0 1 0
# 0 1 0 0 0 0
# 0 0 1 1 1 0
# 1 0 0 0 0 0
# 4 2 3
# 1 6 4