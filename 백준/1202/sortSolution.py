import sys, heapq
input = sys.stdin.readline
N, K = map(int, input().split())
candidates, gems, bags = [], [], []
for _ in range(N):
    weight, cost = map(int, input().split())
    gems.append((weight, cost))
for _ in range(K):
    capacity = int(input())
    bags.append(capacity)

# sort
gems.sort()
bags.sort()

answer = 0
p1 = 0
for p2 in range(K):
    cur_bag = bags[p2]
    while p1 < N and gems[p1][0] <= cur_bag:
        heapq.heappush(candidates, -gems[p1][1])
        p1 += 1
    if candidates:
        answer += -heapq.heappop(candidates)
print(answer)

