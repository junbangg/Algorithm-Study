import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

N, M = len(word1), len(word2)
dp = [[''] * (M+1) for _ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, M+1):
        if word1[x-1] == word2[y-1]:
            dp[x][y] = dp[x-1][y-1] + word1[x-1]
        else:
            if len(dp[x-1][y]) > len(dp[x][y-1]):
                dp[x][y] = dp[x-1][y]
            else:
                dp[x][y] = dp[x][y-1]

print(len(dp[-1][-1]))
print(dp[-1][-1])