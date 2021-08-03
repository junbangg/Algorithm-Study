import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())

dic = collections.defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    dic[b].append(a)

def bfs(start):
    visited = [0] * (N+1)
    q = collections.deque()
    q.append(start)
    visited[start] = 1
    cnt = 0
    while q:
        cur = q.popleft()
        for nxt in dic[cur]:
            if visited[nxt] == 0:
                cnt += 1
                visited[nxt] = 1
                q.append(nxt)
    return cnt

counts = [0] * (N+1)
for i in range(1, N+1):
    counts[i] = bfs(i)
maxCount = max(counts)
for i in range(1, N+1):
    if counts[i] == maxCount:
        print(i, end=' ')
