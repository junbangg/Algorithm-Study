# 1931
import sys, heapq
input = sys.stdin.readline
n = int(input())

h = []
# make heap
for _ in range(n):
    start, end = list(map(int, input().split()))
    heapq.heappush(h, [end, start])

# solve
count = 0
# [start, end]
prev = [0, 0]
while h:
    end, start = heapq.heappop(h)
    if prev[1] <= start:
        count += 1
        prev = [start, end]
print(count)



