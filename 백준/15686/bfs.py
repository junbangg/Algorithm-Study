import sys, itertools, collections
input = sys.stdin.readline
INF = float('inf')
# 입력
N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]


def bfs(src_x, src_y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = collections.deque()
    q.append((src_x, src_y))
    visited[src_x][src_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[x][y] + 1 < visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


# 집이랑 치킨집 좌표 저장
ones, twos = [], []
for x in range(N):
    for y in range(N):
        if town[x][y] == 1:
            ones.append((x, y))
        elif town[x][y] == 2:
            twos.append((x, y))

answer = sys.maxsize
# 가능한 모든 M 개의 치킨집 조합 
for candidates in list(itertools.permutations(twos, M)):
    visited = [[INF] * N for _ in range(N)]
    for x, y in candidates:
        # get minimum from 2 -> 1's
        bfs(x, y)
    total = 0
    for x, y in ones:
        if town[x][y] == 1:
            total += visited[x][y]
    answer = min(answer, total)
print(answer)



