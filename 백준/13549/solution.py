import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
dp = [0 for _ in range(100001)]

def bfs(src):
    q = deque()
    q.append(src)
    while q:
        cur = q.popleft()
        if cur == K:
            return dp[cur]
        for nxt in cur + 1, cur - 1, cur * 2:
            if 0 <= nxt <= 100000 and not dp[nxt]:
                if nxt == cur * 2 and nxt != 0:
                    dp[nxt] = dp[cur]
                    q.appendleft(nxt) # 순간이동을 더 높은 우선순위에 둔다
                else:
                    dp[nxt] = dp[cur] + 1
                    q.append(nxt)
print(bfs(N))
