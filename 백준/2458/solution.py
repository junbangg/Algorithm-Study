import sys
input = sys.stdin.readline
N, M = map(int, input().split())

dp = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    dp[u-1][v-1] = 1

#Floyd-Warshall
for mid in range(N):
    for start in range(N):
        for end in range(N):
            if dp[start][end] == 1 or dp[start][mid] == dp[mid][end] == 1:
                dp[start][end] = 1

answer = 0
for i in range(N):
    known = 0
    for j in range(N):
        known += dp[i][j] + dp[j][i]
    if known == N-1:
        answer += 1

print(answer)