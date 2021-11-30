import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

N, M = len(word1), len(word2)
dp = [[0] * (M+1) for _ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, M+1):
        if word1[x-1] == word2[y-1]:
            dp[x][y] = dp[x-1][y-1] + 1
        else:
            dp[x][y] = max(dp[x-1][y], dp[x][y-1])

print(dp[-1][-1])
            
