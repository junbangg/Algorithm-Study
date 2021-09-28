import sys, collections, heapq
input = sys.stdin.readline
N, M = map(int, input().split())
INF = float('inf')

def dijkstra(src, dest):
    visited = [-INF] * (N + 1)
    visited[src] = INF
    q = []
    heapq.heappush(q, (0, src))
    while q:
        curWeight, cur = heapq.heappop(q)
        # if visited[cur] < curWeight:
            # continue
        while graph[cur]:
            nxt, nxtWeight = graph[cur].pop()
            possibleWeight = min(visited[cur], nxtWeight)
            if visited[nxt] < possibleWeight:
                visited[nxt] = possibleWeight
                heapq.heappush(q, (- nxtWeight, nxt))
    return visited[dest]

graph = collections.defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append([A, C])
src, dest = map(int, input().split())
print(dijkstra(src, dest))

# 4 5
# 1 2 4
# 1 3 5
# 2 3 5
# 2 4 1
# 3 4 5
# 1 4
# -> 5

# 4 5
# 1 2 4
# 1 3 5
# 2 3 4
# 2 4 3
# 3 4 1
# 1 4
# -> 3

# 4 5
# 1 2 4
# 1 3 5
# 2 3 4
# 2 4 3
# 3 4 4
# 1 4
# -> 4