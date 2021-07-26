import sys, heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    heapq.heappush(graph, (cost,a,b))

parent = [i for i in range(N+1)]
# 특정 원소가 속한 집합을 찾는 함수
def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

tree_edges, mst_cost = 0, 0
while True:
    # 가지치기
    if tree_edges == N-1:
        break
    cost, u, v = heapq.heappop(graph)
    if u == v:continue
    elif find(u) != find(v):
        union(u, v)
        mst_cost += cost
        tree_edges += 1
print(mst_cost)