from collections import defaultdict
def solution(n, computers):
    # adjacency list
    graph = defaultdict(list)
    for i in range(n):
        for j in range(len(computers[0])):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    visited = [False] * n
    def dfs(v):
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                dfs(i)
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer
