import sys, heapq, collections
input = sys.stdin.readline
INF = sys.maxsize
def dijkstra(seoul, LA, graph, M, K):
    #준비물
    distance = [INF] * (LA+1)
    costs = [0] * (LA+1)
    #다익스트라
    distance[seoul] = 0
    costs[seoul] = 0
    q = [] # (dist, node)
    q.append((distance[seoul], seoul))
    while q:
        dist, node = heapq.heappop(q)
        if node == LA:
            continue
        if distance[node] < dist:
            continue
        for nxt_node, nxt_cost, nxt_dist in graph[node]:
            if distance[node] + nxt_dist < distance[nxt_node] and costs[node] + nxt_cost <= M:
                distance[nxt_node] = distance[node] + nxt_dist
                costs[nxt_node] = costs[node] + nxt_cost
                q.append((distance[nxt_node], nxt_node))
    return distance[LA]

#입력
tc = int(input())
for _ in range(tc):
    N, M, K = map(int, input().split())
    graph = collections.defaultdict(list)
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    result = dijkstra(1, N, graph, M, K)
    if result == INF:
        print("Poor KCM")
    else:
        print(result)