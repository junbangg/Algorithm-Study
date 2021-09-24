import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
INF = float('inf')
def bfs(src, dest):
    visited = [-INF] * (N + 1)
    visited[src] = INF
    q = collections.deque()
    q.append((src))
    while q:
        cur = q.popleft()
        while graph[cur]:
            nxt, nxtWeight = graph[cur].pop()
            possibleWeight = min(visited[cur], nxtWeight)
            if visited[nxt] < possibleWeight:
                visited[nxt] = possibleWeight
                q.append(nxt)
    return visited[dest]

graph = collections.defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append([A, C])
src, dest = map(int, input().split())
print(bfs(src, dest))
