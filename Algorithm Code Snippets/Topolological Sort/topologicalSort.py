from collections import deque
N, M = map(int, input().split())
prereq = [0] * (N + 1)
graph = {}

# setup prereq and graph
for i in range(N+1):
    graph[i] = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    prereq[b] += 1

# topological sort
def topologicalSort():
    q, answer = deque(), []
    # Add nodes without prerequisite
    for i in range(1, N+1):
        if prereq[i] == 0:
            q.append(i)
    # Sort
    while q:
        cur = q.popleft()
        answer.append(cur)
        for nxt in graph[cur]:
            prereq[nxt] -= 1
            if prereq[nxt] == 0:
                q.append(nxt)
    return answer

