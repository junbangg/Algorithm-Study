import sys, heapq
input = sys.stdin.readline

def dijkstra(src, dest):
    visited = [float('inf')] * (N+1)
    visited[src] = 0
    q = []
    heapq.heappush(q, (0, src))
    while q:
        dist, cur = heapq.heappop(q)
        if visited[cur] < dist:
            continue
        for nxt, nxt_dist in _map[cur]:
            if visited[cur] + nxt_dist < visited[nxt]:
                visited[nxt] = visited[cur] + nxt_dist
                heapq.heappush(q, (visited[nxt], nxt))
    return visited[dest]

N, M, X = map(int, input().split())
_map = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, l = map(int, input().split())
    _map[a].append((b, l))

answer = 0
# i 정점 -> X 정점 까지의 최단거리 + X정점 -> i 정점 까지의 최단거리 중 최대값 구하기
for i in range(1, N+1):
    answer = max(answer, dijkstra(i, X) + dijkstra(X, i))
print(answer)
