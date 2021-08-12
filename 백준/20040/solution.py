import sys

def find(x, parent):
    if parent[x] != x:
        return find(parent[x], parent)
    return x
def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline
N, M = map(int, input().split())
parent = [i for i in range(N)]
for i in range(1, M+1):
    a, b = map(int, input().split())
    if find(a, parent) == find(b, parent):
        print(i)
        exit(0)
    else:
        union(a, b, parent)
print(0)