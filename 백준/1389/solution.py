from collections import defaultdict, deque
N, M = list(map(int, input().split()))
dic = defaultdict(list)
for _ in range(M):
    a, b = list(map(int, input().split()))
    dic[a].append(b)
    dic[b].append(a)


def bfs(node):
    visited = [-1 for _ in range(N+1)]
    visited[node] = 0
    q = deque()
    q.append(node)
    while q:
        cur = q.popleft()
        for nxt in dic[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
    return [sum(visited), node]

answer = []
for i in range(1, N+1):
    answer.append(bfs(i))
print(sorted(answer)[0][1])