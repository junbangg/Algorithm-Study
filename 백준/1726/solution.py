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

def printMap(board):
    for i in range(len(board)):
        print(*board[i])

# Test 해서 (0, 0) 에서 일어나는 변경을 디버깅해볼것.
# (0,0 ) 에서 command 수가 하나 더 더해진다.
def bfs(src_x, src_y, src_dir, dest_x, dest_y, dest_dir): # 전부 1 뺴기
    visited = [[False] * M for _ in range(N)]
    visited[src_x][src_y] = True
    q = collections.deque([(src_x, src_y, src_dir, 0, 0, False)]) # x,  y, 방향, cmds, leap

    while q:
        cur_x, cur_y, cur_dir, cur_cost, leap, leapSwitch = q.popleft()
        # 0, 0, 4, 3
        for nxt_dir in range(4):
            nx, ny = cur_x + dx[nxt_dir], cur_y + dy[nxt_dir]
            minDirectionCommands = getMinDirectionCommand(cur_dir, nxt_dir)
            nxt_cost = cur_cost + minDirectionCommands
            # 방향이 바뀌었다는 뜻
            if minDirectionCommands > 0:
                nxt_cost += 1
                leap = 0
                leapSwitch = False
            else:
                if not leapSwitch:
                    nxt_cost += 1
                leapSwitch = True
                leap += 1
            if leap == 3:
                #nxt_cost += 1
                leap = 0
                leapSwitch = False
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and _map[nx][ny] == '0':
                visited[nx][ny] = True
                print("nx, ny, nxt_cost, leap", nx, ny, nxt_cost, leap)
                if nx == dest_x and ny == dest_y:
                    return nxt_cost + getMinDirectionCommand(nxt_dir, dest_dir)
                q.append((nx, ny, nxt_dir, nxt_cost, leap, leapSwitch))

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

