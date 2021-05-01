def dfs(v, count):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, count+1)
    
visited = [False] * n
