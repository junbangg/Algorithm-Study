import heapq, sys
input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    cmd = int(input())
    if cmd == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)
    else: 
        heapq.heappush(h, -cmd)

