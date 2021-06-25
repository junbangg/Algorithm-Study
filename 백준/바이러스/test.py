def dfs(node):
    global count
    while dic[node]:
        v = dic[node].pop()
        if not visited[v-1]:
            count += 1
            visited[v-1] = True
            dfs(v)
    return


