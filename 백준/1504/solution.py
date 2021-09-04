# - C -> C 까지의 최단거리
# - 방향을 몇 번 꺾는지 계산 해야함
#     - SW / NE 방향을 매번 저장해서, 바뀔때마다 체크
# BFS 로 구현

# q 에 (next_x, next_y, 통신 방향) 식으로 적재

import sys, heapq
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
corner = ['NS', 'NS', 'WE', 'WE']

def printBoard(board):
    
    for i in range(len(board)):
        print(*board[i])
    print('\n')


def dijkstra(src_x, src_y, dest_x, dest_y):
    visited = [[float('inf')] * M for _ in range(N)]
    visited[src_x][src_y] = 0
    q = []
    heapq.heappush(q, (0, src_x, src_y, ''))
    answer = float('inf')
    while q:
        cnt, cur_x, cur_y, dir = heapq.heappop(q)
        # if visited[cur_x][cur_y] < cnt:
        #     continue
        if cur_x == dest_x and cur_y == dest_y:
            answer = min(answer, cnt)
            printBoard(visited)
            continue
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and _map[nx][ny] != '*':
                nxt_dir, nxt_cnt = corner[i], cnt
                # 코너 돌면 nxt_cnt에 1 추가
                if dir != '' and nxt_dir != dir:
                    nxt_cnt += 1
                    # print('corner! x, y, cnt', nx, ny, nxt_cnt)
                    # printBoard(visited)
                # C 도착: 최소값 갱신
                # if nx == dest_x and ny == dest_y:
                    # answer = min(answer, nxt_cnt)
                    # visited[nx][ny] = min(visited[nx][ny], nxt_cnt)
                    # continue
                # 최소 경로만 탐색
                if nxt_cnt <= visited[nx][ny]:
                    visited[nx][ny] = nxt_cnt
                    printBoard(visited)
                    heapq.heappush(q, (nxt_cnt, nx, ny, nxt_dir))
    # printBoard(visited)
    # return visited[dest_x][dest_y]
    return answer



M, N = map(int, input().split())
_map = [list(input().rstrip()) for _ in range(N)]
c = []
for x in range(N):
    for y in range(M):
        if _map[x][y] == 'C':
            c.append(x)
            c.append(y)
print(dijkstra(c[0], c[1], c[2], c[3]))

# 7 8
# ....*.C
# .****.C
# ....*.*
# *.***.*
# ....*..
# ....*..
# ....*..
# .......



# 1 2
# C
# C

# 2 1
# CC