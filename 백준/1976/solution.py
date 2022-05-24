import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, a, b):
    aParent = find(parent, a)
    bParent = find(parent, b)
    if aParent < bParent:
        parent[bParent] = aParent
    else:
        parent[aParent] = bParent

N = int(input())
M = int(input())

parents = [i for i in range(N)]

for i in range(N):
    data = map(int, input().split())

    for j, isPath in enumerate(data):
        if isPath:
            union(parents, i, j)
travelPath = list(map(int, input().split()))

for i in range(1, len(travelPath)):
    start = travelPath[i-1] - 1
    destination = travelPath[i] - 1

    if find(parents, start) != find(parents, destination):
        print("NO")
        exit(0)
print("YES")