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

def bfs(src_x, src_y, src_dir, dest_x, dest_y, dest_dir): # 전부 1 뺴기
    visited = [[False] * M for _ in range(N)]
    visited[src_x][src_y] = True
    # q = collections.deque([(src_x, src_y, src_dir, 0, 0)]) # x,  y, 방향, cmds, leap
    q = []
    heapq.heappush(q, [0, src_x, src_y, src_dir, 0])

    while q:
        # cur_x, cur_y, cur_dir, cur_cost, leap = q.popleft()
        cur_cost, cur_x, cur_y, cur_dir, leap = heapq.heappop(q)
        for nxt_dir in range(4):
            nx, ny = cur_x + dx[nxt_dir], cur_y + dy[nxt_dir]
            minDirectionCommands = getMinDirectionCommand(cur_dir, nxt_dir)
            nxt_cost = cur_cost + minDirectionCommands
            if minDirectionCommands > 0:
                nxt_cost += 1
            else:
                if leap == 0:
                    nxt_cost += 1
                leap += 1
            if leap == 3:
                leap = 0
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and _map[nx][ny] == '0':
                visited[nx][ny] = True
                print("nx, ny, nxt_cost, leap", nx, ny, nxt_cost, leap)
                if nx == dest_x and ny == dest_y:
                    # print("도착: cost, cur_dir, dest_dir, directionCost", nxt_cost, nxt_dir, dest_dir, getMinDirectionCommand(nxt_dir, dest_dir))
                    return nxt_cost + getMinDirectionCommand(nxt_dir, dest_dir)
                # if leap > 0:
                    # q.appendleft((nx, ny, nxt_dir, nxt_cost, leap))
                else:
                    # q.append((nx, ny, nxt_dir, nxt_cost, leap))
                    heapq.heappush(q, [nxt_cost, nx, ny, nxt_dir, leap])

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