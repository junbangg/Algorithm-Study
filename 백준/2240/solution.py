import sys
input = sys.stdin.readline
N, HP = map(int, input().split())
plums = [0] + [int(input()) for _ in range(N)]
dp = [[0] * (HP+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(HP+1):
        # 짝수 == 1번 나무   //   홀수 == 2번 나무
        if j % 2 == 0 and plums[i] == 1 or j % 2 == 1 and plums[i] == 2:
            if j == 0:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            if j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[-1]))