import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())

# 거리 저장
dist = [INF] * (N+1)
# 간선 정보
edges = []
for _ in range(M):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))

def belmanFord(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            cur, nxt, weight = edges[j]
            if dist[cur] != INF and dist[nxt] > dist[cur] + weight:
                dist[nxt] = dist[cur] + weight
                if i == N-1:
                    return True
    return False


isCycle = belmanFord(1)
if isCycle:
    print("-1")
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])