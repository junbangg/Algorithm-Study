import sys, heapq
input = sys.stdin.readline

h = []
N = int(input())
for _ in range(N):
    heapq.heappush(h, int(input()))
answer = 0
while len(h) != 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    answer += a+b
    heapq.heappush(h, a+b)
print(answer)