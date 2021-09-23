import sys, collections, heapq
input = sys.stdin.readline
N, M = map(int, input().split())
INF = float('inf')
def bfs(src, dest):
    visited = [-INF] * (N + 1)
    visited[src] = INF
    # q = collections.deque()
    # q.append((src))
    q = []
    heapq.heappush(q, (0, src))

    while q:
        # cur = q.popleft()
        curWeight, cur = heapq.heappop(q)
        if visited[cur] < curWeight:
            continue
        # for nxt, nxtWeight in graph[cur]:
            # possibleWeight = min(visited[cur], nxtWeight)
        while graph[cur]:
            nxt, nxtWeight = graph[cur].pop()
            possibleWeight = min(visited[cur], nxtWeight)
            if visited[nxt] < possibleWeight:
                visited[nxt] = possibleWeight
                # q.append(nxt)
                heapq.heappush(q, (- nxtWeight, nxt))
    return visited[dest]

graph = collections.defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append([A, C])
src, dest = map(int, input().split())
print(bfs(src, dest))

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