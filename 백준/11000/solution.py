import sys, heapq
N = int(input())
data = sorted([list(map(int, input().split())) for _ in range(N)])

rooms = []
for start, end in data:
    if rooms and start >= rooms[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, end)
print(len(rooms))