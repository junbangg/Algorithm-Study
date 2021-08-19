import sys, collections, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(src_time, src_node):
    q = []
    visited[src_node] = 0
    heapq.heappush(q, (src_time, src_node))
    while q:
        time, node = heapq.heappop(q)
        if visited[node] < time:
            continue
        for nxt_node, nxt_time in graph[node]:
            if visited[nxt_node] > time + nxt_time:
                visited[nxt_node] = time + nxt_time
                heapq.heappush(q, (time + nxt_time, nxt_node))

tc = int(input())
for _ in range(tc):
    N, D, S = map(int, input().split())
    graph = collections.defaultdict(list)
    for _ in range(D):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    visited = [INF] * (N+1)
    dijkstra(0, S)
    count, maxDist = 0, 0
    for i in visited:
        if i != INF:
            count += 1
            maxDist = max(maxDist, i)
    print(count, maxDist)