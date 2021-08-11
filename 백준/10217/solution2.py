import sys, heapq, collections
input = sys.stdin.readline
INF = sys.maxsize
def dijkstra(graph, N, M):
    dp = [[INF for _ in range(M+1)] for _ in range(N+1)]
    dp[1][0] = 0
    for cur_cost in range(M+1):
        for cur_node in range(1, N+1):
            if dp[cur_node][cur_cost] == INF:
                continue
            distance = dp[cur_node][cur_cost]
            for nxt, nxt_cost, nxt_dist in graph[cur_node]:
                if cur_cost + nxt_cost > M:
                    continue
                dp[nxt][cur_cost+nxt_cost] = min(dp[nxt][cur_cost + nxt_cost], distance + nxt_dist)
    return dp

#입력
tc = int(input())
for _ in range(tc):
    N, M, K = map(int, input().split())
    graph = collections.defaultdict(list)
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))

    result = dijkstra(graph, N, M)
    print(result)
    if min(result[N]) == INF:
        print("Poor KCM")
    else:
        print(min(result[N]))
    