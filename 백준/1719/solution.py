import sys, heapq
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dijkstra(start):
    q = []
    heapq.heappush((q, (0, start)))
    dp = [float('inf') for _ in range(N + 1)]
    dp[start] = 0
    while q:
        weight, cur = heapq.heappop(q)
        for nxt, nxt_weight in _map[cur]:
            new_weight = nxt_weight + weight
            if dp[nxt] > new_weight:
                dp[nxt] = new_weight
                heapq.heappush(q, (new_weight, nxt))
                visited[nxt - 1][start - 1] = cur

N, M = map(int, input().split())
_map = [[] for i in range(N + 1)]
visited = [[0] * N for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    _map[a].append([b, c])
    _map[b].append([a, c])
for i in range(1, N + 1):
    dijkstra(i)
for i in range(N):
    for j in range(N):
        if i == j:
            print("-", end=" ")
        else:
            print(visited[i][j], end=" ")
    print('\n')