import sys
input = sys.stdin.readline

N, E = map(int, input().split())
_map = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    _map[a].append((b, c))
    _map[b].append((a, c))
v1, v2 = map(int, input().split())

visited = [[float('inf')] * (N+1) for _ in range(N+1)]
# 그래프 초기화
for a in range(1, N+1):
    for b, c in _map[a]:
        visited[a][b] = min(visited[a][b], c)

for mid in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            if start != end:
                visited[start][end] = min(visited[start][end], visited[start][mid] + visited[mid][end])

answer = float('inf')

# v1_start = visited[1][v1] + visited[v1][v2] + visited[v2][N]
# v2_start = visited[1][v2] + visited[v2][v1] + visited[N][v2]

answer = min(visited[1][v1] + visited[v1][v2] + visited[v2][N], visited[1][v2] + visited[v2][v1] + visited[N][v2])
print(answer if answer != float('inf') else -1)
    







