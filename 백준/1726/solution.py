import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
_map = [input().split() for _ in range(N)]
src = list(map(int, input().split()))
dest = list(map(int, input().split()))

# 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

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
    q = collections.deque([(src_x, src_y, src_dir, 0, 0)]) # x,  y, 방향, cmds, leap

    while q:
        cur_x, cur_y, cur_dir, cur_cost, leap = q.popleft()
        if cur_x == dest_x and cur_y == dest_y:
            if cur_dir != dest_dir:
                print("같은 방향 아님")
                cur_cost += getMinDirectionCommand(cur_dir, dest_dir)
            print("도착스: cur_dir, nxt_cost", cur_dir, cur_cost)
            return cur_cost
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            minDirectionCommands = getMinDirectionCommand(cur_dir, i)
            nxt_cost = cur_cost + minDirectionCommands
            if minDirectionCommands > 0:
                nxt_cost += 1
            else:
                leap += 1
                if leap > 3:
                    nxt_cost += 1
                    leap = 0
            #nxt_cost = cur_cost + minimumDirectionCommand(cur_dir, i) + 1
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and _map[nx][ny] == '0':
                #if nx == dest_x and ny == dest_y:
                    #print("도착스: cur_dir, nxt_cost", cur_dir, nxt_cost)
                    #return nxt_cost
                visited[nx][ny] = True
                print("nx, ny, nxt_cost", nx, ny, nxt_cost)
                q.append((nx, ny, i, nxt_cost, leap))

print(bfs(src[0]-1, src[1]-1, src[2]-1, dest[0]-1, dest[1]-1, dest[2]-1))