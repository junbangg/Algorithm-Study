import sys, collections
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

test = [(3, 1), (3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (3, 1)]
test2 = [(3, 1), (4, 1), (4, 2), (4, 3), (4,4), (4, 5), (3, 5), (2, 5), (2, 4)]
def bfs(src_x, src_y, src_dir, dest_x, dest_y, dest_dir): # 전부 1 뺴기
    visited = [[False] * M for _ in range(N)]
    visited[src_x][src_y] = True
    q = collections.deque([(src_x, src_y, src_dir, 0, 0)]) # x,  y, 방향, cmds, leap
    while q:
        cur_x, cur_y, cur_dir, cur_cost, cur_leap = q.popleft()
        for nxt_dir in range(4):
            nx, ny = cur_x + dx[nxt_dir], cur_y + dy[nxt_dir]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and _map[nx][ny] == '0':
                visited[nx][ny] = True
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
                if (nx, ny) in test2:
                    print("nx, ny, nxt_cost, leap", nx, ny, nxt_cost, nxt_leap)
                if nx == dest_x and ny == dest_y:
                    # print("도착: cost, cur_dir, dest_dir, directionCost", nxt_cost, nxt_dir, dest_dir, getMinDirectionCommand(nxt_dir, dest_dir))
                    return nxt_cost + getMinDirectionCommand(nxt_dir, dest_dir)
                q.append((nx, ny, nxt_dir, nxt_cost, nxt_leap))

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