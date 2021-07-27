import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾는 함수
def find(x):
    if parent[x] != x:
        root = find(parent[x])
        dp[x] += dp[parent[x]]
        parent[x] = root
        return parent[x]
    return x

# 두 원소가 속한 집합을 합치기
def union(a, b, weight):
    x, y = parent[a], parent[b]
    if x != y:
        parent[y] = x
        dp[y] = (dp[a] + weight) - dp[b]

while 1:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    parent = [i for i in range(N+1)]
    dp = [0 for i in range(N+1)]
    for _ in range(M):
        inp = input().split()
        find(int(inp[1]))
        find(int(inp[2]))
        if inp[0] == '!':
            #union
            union(int(inp[1]), int(inp[2]), int(inp[3]))
        elif inp[0] == '?':
            #find
            if parent[int(inp[1])] == parent[int(inp[2])]:
                print(dp[int(inp[2])] - dp[int(inp[1])])
            else:
                print("UNKNOWN")