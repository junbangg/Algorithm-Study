import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, color):
    visited[node] = color
    for nxt in graph[node]:
        if visited[nxt] == 0:
            if not dfs(nxt, -color):
                return False
        elif visited[node] == visited[nxt]:
            return False
    return True

tc = int(input())
for _ in range(tc):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    bipartrite = True
    for i in range(1, V+1):
        if visited[i] == 0:
            bipartrite = dfs(i, 1)
            if not bipartrite:
                break
    if bipartrite:
        print("YES")
    else:
        print("NO")
