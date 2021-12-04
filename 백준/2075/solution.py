import sys, heapq
input = sys.stdin.readline

N = int(input())
h = []
for num in map(int, input().split()):
    heapq.heappush(h, num)
for _ in range(1, N):
    for num in map(int, input().split()):
        heapq.heappush(h, num)
        heapq.heappop(h)
print(h[0])