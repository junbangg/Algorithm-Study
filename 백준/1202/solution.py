import sys, heapq
input = sys.stdin.readline
N, K = map(int, input().split())
candidates, gems, bags = [], [], []
for _ in range(N):
    weight, cost = map(int, input().split())
    heapq.heappush(gems, (weight, cost))
for _ in range(K):
    heapq.heappush(bags, int(input()))

answer = 0
for _ in range(K):
    bag = heapq.heappop(bags)
    while gems and bag >= gems[0][0]:
        gem_weight, gem_cost = heapq.heappop(gems)
        heapq.heappush(candidates, -gem_cost)
    if candidates:
        answer += -heapq.heappop(candidates)
print(answer)