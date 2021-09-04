#다익스트라
import heapq
input = __import__('sys').stdin.readline
m,n = map(int, input().split())
mp = [input() for _ in range(n)]
visit = [[float("inf")] * m for _ in range(n)]
check = 0
sy = sx = ey = ex = -1
ly,lx = [1,-1,0,0],[0,0,-1,1]
for i in range(n):
    for j in range(m):
        if mp[i][j] == 'C' and check == 0:
            sy,sx = i,j
            check+=1
        elif mp[i][j] == 'C':
            ey,ex = i,j
            break
#0,1,2,3 하상좌우
#들어가는 데이터는 (꺾은 회수,현재 방향,y,x)
ans = float("inf")
visit[sy][sx] = 0
q = []
heapq.heappush(q,(0,0,sy,sx))
heapq.heappush(q,(0,1,sy,sx))
heapq.heappush(q,(0,2,sy,sx))
heapq.heappush(q,(0,3,sy,sx))
while q:
    turned,nowdir,y,x = heapq.heappop(q)
    if y == ey and x == ex:
        ans = min(turned,ans)
    else:
        for i in range(4):
            ny,nx = y + ly[i],x + lx[i]
            if 0 <= ny < n and 0 <= nx < m and mp[ny][nx] != '*':
                if i != nowdir and visit[ny][nx] >= turned + 1:
                    visit[ny][nx] = turned + 1
                    heapq.heappush(q,(turned + 1,i,ny,nx))
                elif i == nowdir and visit[ny][nx] >= turned:
                    visit[ny][nx] = turned
                    heapq.heappush(q,(turned,nowdir,ny,nx))
print(ans)