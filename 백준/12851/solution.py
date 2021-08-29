import sys, collections
input = sys.stdin.readline
INF = float('inf')

def bfs(src, dest):
    visited = [INF] * 100001
    q = collections.deque()
    q.append(src)
    visited[src] = 0
    paths = 0  # 최단거리로 dest에 도착할때마다 여기다가 기록한다

    while q:
        cur = q.popleft()
        if cur == dest and visited[dest] != INF: # 도착을 했고 최단거리가 계산 되었을때, paths에 추가
            paths += 1
        for nxt in [cur+1, cur-1, cur*2]:
            if 0 <= nxt < 100001 and visited[cur] + 1 <= visited[nxt]:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
    return visited[dest], paths # 최솟값, 최솟값으로 도착한 경우의 수를 반환

N, K = map(int, input().split())
minTime, paths = bfs(N, K)
print(minTime)
print(paths)