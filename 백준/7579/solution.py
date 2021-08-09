import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())
h = []
apps = list(map(int, input().split()))
costs = list(map(int, input().split()))
for i in range(N):
    heapq.heappush(h, ((costs[i], apps[i])))
memory, answer = 0, 0
while h and memory < M:
    c, m = heapq.heappop(h)
    memory += m
    answer += c
print(answer)