import sys, collections
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())
dist = [[INF] * (N) for _ in range(N)]
graph = collections.defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

#graph 초기화
for a in graph.keys():
    for b, c in graph[a]:
        dist[a-1][b-1] = c
        # dist[a-1][b-1] = min(dist[a-1][b-1], c)

for mid in range(N):
    for start in range(N):
        for end in range(N):
            if start != end:
                dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])

for i in range(N):
    for j in range(N):
        if dist[i][j] == INF:
            dist[i][j] = 0
    print(*dist[i])
