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

#입력
N, M, R = map(int, input().split())
items = [0] + [i for i in map(int, input().split())]
_map = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    _map[a].append((b, l))
    _map[b].append((a, l))


answer = 0
for i in range(1, N+1): # 모든 정점에 대해 dijkstra 수행
    visited = dikjstra(i) # i -> 모든 정점까지의 최소거리 계산
    total = 0
    for j in range(1, N+1): # 최소 거리가 수색범위(M) 이하이면 아이템 수 더하기
        if visited[j] <= M:
            total += items[j]
    answer = max(answer, total) # 아이템 합 최대 갱신
print(answer)

