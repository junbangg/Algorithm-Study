import sys, heapq
input = sys.stdin.readline

h = []
N = int(input())
for _ in range(N):
    heapq.heappush(h, int(input()))

total = 0
while len(h) >= 2:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    total += a + b
    heapq.heappush(h, a+b)
print(total)