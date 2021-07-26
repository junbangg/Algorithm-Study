import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
height = [0] * (N+1)
graph = {}

# 초기화
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    height[b] += 1

# 위상정렬
q, answer = collections.deque(), []

#선행 정점 없는 것 큐에 추가
for i in range(1, N+1):
    if height[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    answer.append(cur)
    for nxt in graph[cur]:
        height[nxt] -= 1
        if height[nxt] == 0:
            q.append(nxt)
print(*answer)
