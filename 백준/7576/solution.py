import sys, collections
input = sys.stdin.readline
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(q, count):
    answer = -sys.maxsize
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0<=nx<N and 0<=ny<M and grid[nx][ny] == 0:
                grid[nx][ny] = grid[cur_x][cur_y] + 1
                answer = max(answer, grid[nx][ny])
                count -= 1
                q.append((nx, ny))
    return (answer, count)

tomatos, count = collections.deque(), 0
# first traversal 
for i in range(N):
    for j in range(M):
        # 익은 토마토 큐에 저장
        if grid[i][j] == 1:
            tomatos.append((i, j))
        # 안 익은 토마토 개수 세기
        if grid[i][j] == 0:
            count += 1
# base case: 다 익은 경우
if count == 0:
    print(0)
    exit(0)
#BFS
answer, count = bfs(tomatos, count)
if count != 0:
    print(-1)
else:
    print(answer-1)
