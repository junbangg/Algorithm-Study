import sys, collections
input = sys.stdin.readline

N = int(input())
costs = [0] * (N+1)
answer = [0] * (N+1)
parent = [0] * (N+1)

#graph 생성
graph = collections.defaultdict(list)
# 초기화
for i in range(1, N+1):
    data = list(map(int, input().split()))[:-1]
    costs[i] = data[0]
    for pre in data[1:]:
        graph[pre].append(i)
        parent[i] += 1

q = collections.deque()
for i in range(1, N+1):
    if parent[i] == 0:
        q.append(i)
        answer[i] = costs[i]

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        answer[nxt] = max(answer[nxt], costs[nxt] + answer[cur])
        parent[nxt] -= 1
        if parent[nxt] == 0:
            q.append(nxt)
for a in answer[1:]:
    print(a)