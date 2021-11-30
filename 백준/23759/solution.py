import sys
input = sys.stdin.readline
N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dp = [[0] * (N+1) for _ in range(27)]

# set dp
# for letter in words[0]:
#     letterIndex = ord(letter) - 97
#     dp[letterIndex][0] += 1

for i in range(1, 27):
    for j in range(1, len(words)+1):
        if alphabet[i-1] in words[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# for i in range(len(dp)):
    # print(*dp[i])
print(N - dp[-1][-1])



# 5 1
# a
# b
# b
# b
# a