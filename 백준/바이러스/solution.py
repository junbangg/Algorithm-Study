from collections import defaultdict
n = int(input())
pairs = int(input())

dic = defaultdict(list)
visited = [False] * n
visited[0] = True

for _ in range(pairs):
    a, b = list(map(int, input().split()))
    dic[a].append(b)
    dic[b].append(a)

count = 0
def dfs(node):
    global count
    for v in dic[node]:
        if not visited[v-1]:
            count += 1
            visited[v-1] = True
            dfs(v)
    return
dfs(1)
print(count)

