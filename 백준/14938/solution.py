import sys, heapq
input = sys.stdin.readline

# 1. nxt 정점으로 이동
#   - a. 누적 거리가 m 이하 인지 확인
#   - b. 아이템 추가

def dikjstra(src):
    dp = [float('inf')] * (N+1)
    dp[src] = 0
    q = []
    heapq.heappush(q, (0, src)) # 거리, 정점
    while q:
        dist, cur_v = heapq.heappop(q)
        # 최적화 조건
        if dp[cur_v] < dist:
            continue
        for nxt_v, nxt_dist in  _map[cur_v]:
            if dp[cur_v] + nxt_dist < dp[nxt_v]:
                dp[nxt_v] = dp[cur_v] + nxt_dist
                heapq.heappush(q, (nxt_dist, nxt_v))
    return dp

N, M, R = map(int, input().split())
items = [0] + [i for i in map(int, input().split())]
_map = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    _map[a].append((b, l))
    _map[b].append((a, l))


answer = 0
for i in range(1, N+1):
    visited = dikjstra(i)
    total = 0
    for j in range(1, N+1):
        if visited[j] <= M:
            total += items[j]
    answer = max(answer, total)
print(answer)

