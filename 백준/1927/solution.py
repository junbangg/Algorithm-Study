import sys
import heapq
input = sys.stdin.readline
N = int(input())
h = []
for _ in range(N):
    cmd = int(input())
    if cmd == 0:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, cmd)





