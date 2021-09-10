import heapq
def solution(n, s, a, b, fares):
    # 그래프 설정
    graph = [[] for _ in range(n+1)]
    for src, dist, cost in fares:
        graph[src].append([dist, cost])
        graph[dist].append([src, cost])
    # 다익스트라
    def dijkstra(src, dest):
        dp = [float('inf') for _ in range(len(graph))]
        dp[src] = 0
        q = []
        heapq.heappush(q, (0, src))
        while q:
            cost, cur = heapq.heappop(q)
            for nxt, nxt_cost in graph[cur]:
                if dp[cur] + nxt_cost < dp[nxt]:
                    dp[nxt] = dp[cur] + nxt_cost
                    heapq.heappush(q, (dp[nxt], nxt))
        return dp[dest]
    
    # 모든 가능한 경유지를 i 로 설정하고
    # [s -> i] + [i -> a] + [i -> b] 까지의 최솟값이 답이 됨
    cost = float('inf')
    for i in range(1, n+1):
        cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    
    return cost