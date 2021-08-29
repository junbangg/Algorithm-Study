import sys, collections
input = sys.stdin.readline
INF = float('inf')

def bfs(src, dest):
    visited = [INF] * 100001
    q = collections.deque()
    q.append(src)
    visited[src] = 0
    candidates = []
    while q:
        cur = q.popleft()
        if cur == dest and visited[dest] != INF:
            candidates.append(visited[dest])
        for nxt in [cur+1, cur-1, cur*2]:
            if 0 <= nxt < 100001 and visited[cur] + 1 <= visited[nxt]:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
    return visited[dest], candidates

N, K = map(int, input().split())
minTime, cands = bfs(N, K)
paths = 0
for c in cands:
    if c == minTime:
        paths += 1
print(minTime)
print(paths)