import sys, heapq
input = sys.stdin.readline

def dijkstra(src):
    dp = [float('inf')] * (N+1)
    q = []
    heapq.heappush(q, (0, src))
    dp[src] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if dp[cur] < dist:
            continue
        for nxt, nxt_dist in _map[cur]:
            if dp[cur] + nxt_dist < dp[nxt]:
                dp[nxt] = dp[cur] + nxt_dist
                heapq.heappush(q, (dp[nxt], nxt))
    return dp



N, E = map(int, input().split())
_map = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    _map[a].append((b, c))
    _map[b].append((a, c))
v1, v2 = map(int, input().split())

# 1 -> v1 -> v2 -> n
# 1 -> v2 -> v1 -> n

start = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

answer = min(start[v1] + from_v1[v2] + from_v2[N], start[v2] + from_v2[v1] + from_v1[N])

print(answer if answer != float('inf') else -1)