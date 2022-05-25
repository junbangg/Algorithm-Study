import sys
from collections import deque
input =sys.stdin.readline
n, t = map(int, input().split())

graph = set()
for _ in range(n):
    x, y = map(int, map(int, input().split()))
    graph.add((x,y))

dx = [-2, -1, 0, 1, 2]
dy = [-2, -1, 0, 1, 2]

q = deque()
q.append([0,0,0])
check = False
while q:
    x, y, cnt = q.popleft()
    if y == t:
        check = True
        break
    for i in range(5):
        for j in range(5):
            nx = x + dx[i]
            ny = y + dy[j]
            if (nx, ny) in graph:
                q.append([nx, ny, cnt+1])
                graph.remove((nx,ny))
        
if check:
    print(cnt)
else:
    print(-1)