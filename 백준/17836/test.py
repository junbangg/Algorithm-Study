import sys, heapq
input = sys.stdin.readline
N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def printBoard(board):
    print('\n')
    for i in range(len(board)):
        print(*board[i])

def dijkstra():
    visited = [[INF] * M for _ in range(N)]
    visited[0][0] = 0
    q = []
    heapq.heappush(q, (1, 0, 0, 0)) # sword(1 is no sword), time, x, y
    while q:
        sword, time, cur_x, cur_y = heapq.heappop(q)
        if visited[cur_x][cur_y] < time:
            continue
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[cur_x][cur_y] + 1 < visited[nx][ny]:
                # sword version
                if sword == 0:
                    visited[nx][ny] = visited[cur_x][cur_y] + 1
                    heapq.heappush(q, (sword, visited[nx][ny], nx, ny))
                elif board[nx][ny] != 1:
                    if board[nx][ny] == 2:
                        sword = 0
                    visited[nx][ny] = visited[cur_x][cur_y] + 1
                    heapq.heappush(q, (sword, visited[nx][ny], nx, ny))
    printBoard(visited)
    return visited[N-1][M-1]

res = dijkstra()
if res == INF or res > T:
    print('Fail')
else:
    print(res)