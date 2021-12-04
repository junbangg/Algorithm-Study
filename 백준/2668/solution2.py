import sys, collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())
graph = collections.defaultdict(list)
for i in range(1, N+1):
    graph[int(input().rstrip())].append(i)

def dfs(index, visited):
    visited.add(index)
    checked[index] = 1
    for v in graph[index]:
        if v in visited:
            result.extend(list(visited))
            return
        else:
            dfs(v, visited.copy())

checked = [0 for _ in range(N+1)]
result = []
for i in range(1, N+1):
    if not checked[i]:
        dfs(i, set([]))

result.sort()
print(len(result))
for num in result:
    print(num)
