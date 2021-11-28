import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
_map = [list(input().rstrip()) for _ in range(N)]

dx, dy = [1,-1,0,0], [0,0,1,-1]

def bfs(src_x, src_y):
    global answer
    visited = [[False] * M for _ in range(N)]
    q = collections.deque([])
    q.append([0, src_x, src_y])
    visited[src_x][src_y] = True
    while q:
        cur_dist, cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and _map[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = True
                answer = max(answer, cur_dist + 1)
                q.append([cur_dist+1, nx, ny])

answer = -float('inf')
for x in range(N):
    for y in range(M):
        if _map[x][y] == 'L':
            bfs(x, y)
print(answer)
