import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾는 함수
def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

# 두 원소가 속한 집합을 합치기
def union(parent, a, b):
    aParent = find(parent, a)
    bParent = find(parent, b)
    if aParent < bParent:
        parent[bParent] = aParent
    else:
        parent[aParent] = bParent

N, M = map(int, input().split())
# 초기화
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

# inputs
for _ in range(M):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        #union
        if a != b:
            union(parent, a, b)
    else:
        # find
        if a == b or find(parent, a) == find(parent, b):
            print('YES')
        else:
            print('NO')