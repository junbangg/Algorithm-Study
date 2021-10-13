import sys, heapq
input = sys.stdin.readline
N = int(input())
K = int(input())
_map = [[i*j for i in range(1, N+1)] for j in range(1, N+1)]

dx = [1, 0, 1]
dy = [0, 1, 1]

def bfs():
    visited = [[False] * N for _ in range(N)]
    q = []
    visited[0][0] = True
    heapq.heappush(q, (_map[0][0], 0, 0)) # val, x, y
    count = -1
    while q:
        val, x, y = heapq.heappop(q)
        count += 1
        if count == K:
            return val
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(q, (_map[nx][ny], nx, ny))

print(bfs())
