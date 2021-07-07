from collections import deque
N, K = map(int, input().split())
seconds = [0 for _ in range(1000001)]
answer = 0
def bfs(start):
    q = deque()
    q.append(start)
    seconds[start] = 0
    while q:
        cur = q.popleft()
        if cur == K:
            print(seconds[cur])
            break
        for nxt in (cur + 1, cur - 1, cur * 2):
            if 0 <= nxt <= 1000000 and not seconds[nxt]:
                seconds[nxt] = seconds[cur] + 1
                q.append(nxt)
bfs(N)
   