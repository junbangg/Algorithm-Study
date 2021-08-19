import sys, collections
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]
for length in range(N):
    for start in range(N-length):
        end = start + length
        if start == end: 
            dp[start][end] = 1
        elif nums[start] == nums[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])
