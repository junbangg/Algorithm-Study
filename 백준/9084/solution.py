import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for target in range(1, M+1):
            if target - coin >= 0:
                dp[target] += dp[target-coin]
    print(dp[-1])