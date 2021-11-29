import sys
input = sys.stdin.readline
N, K = map(int, input().split())
# dp = [[0] * N for _ in range(26)]
dp = [0] * 26

answer = 0
for _ in range(N):
    word = list(input().rstrip())
    for letter in set(word):
        dp[ord(letter) - 97] += 1
        answer = max(answer, dp[ord(letter) - 97])
# print(dp
print(N - answer)

# answer = N - 가장 자주 나타나는 letter count 