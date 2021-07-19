import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N = int(input())

# create map
dp = [sys.maxsize] * 50000
def recurse(ind, length, total):
    global answer
    if total >= N:
        return
    
    for i in range(ind, 224):
        if total+i**2 < N:
            dp[total+i**2] = min(length+1, dp[total+i**2])
            recurse(i, length+1, total+i**2)

recurse(1, 0, 0)
print(dp[N])