import sys
input = sys.stdin.readline
N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
dp = [[0] * N for _ in range(26)]

for letter in words[0]:
    letterIndex = ord(letter) - 97
    dp[letterIndex][0] += 1

answer = -float('inf')
for i in range(26):
    for j in range(1, len(words)):
        for letter in words[j]:
            letterIndex = ord(letter) - 97
            if i == letterIndex:
                dp[i][j] = dp[i][j-1] + 1
                answer = max(answer, dp[i][j])
            else:
                dp[i][j] = dp[i][j-1]
print(N - answer)

