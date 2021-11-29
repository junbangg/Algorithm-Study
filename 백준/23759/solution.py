import sys
input = sys.stdin.readline
N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dp = [[0] * N for _ in range(26)]

# set dp
for letter in words[0]:
    letterIndex = ord(letter) - 97
    dp[letterIndex][0] += 1

answer = -float('inf')
for i in range(26):
    for j in range(1, len(words)):
        if alphabet[i] in words[j]:
            dp[i][j] = dp[i][j-1] + 1
            answer = max(answer, dp[i][j])
        else:
            dp[i][j] = dp[i][j-1]

# for i in range(len(dp)):
#     print(*dp[i])
print(N - answer)

