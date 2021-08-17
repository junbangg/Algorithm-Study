import sys
input = sys.stdin.readline
num = list(map(int, input().rstrip()))
dp = [0] * (len(num) + 1)
if num[0] == 0:
    print(0)
    exit(0)
num = [0] + num
dp[0] = dp[1] = 1
for i in range(2, len(num)):
    if 1 <= num[i] <= 10:
        dp[i] += dp[i-1]
    if 10 <= 10 * num[i-1] + num[i] <= 26:
        dp[i] += dp[i-2]
    dp[i] %= 1000000
print(dp[-1])