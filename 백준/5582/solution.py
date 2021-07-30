import sys
input = sys.stdin.readline
s1 = list(input())[:-1]
s2 = list(input())[:-1]
N, M = len(s2), len(s1)
dp = [[0]*(M+1) for _ in range(N+1)]
answer = 0
for x in range(1, N+1):
    for y in range(1, M+1):
        if s1[y-1] == s2[x-1]:
            dp[x][y] += dp[x-1][y-1] + 1
            answer = max(answer, dp[x][y])
print(answer)