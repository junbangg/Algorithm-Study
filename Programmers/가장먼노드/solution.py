from collections import defaultdict
def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a-1].append(b-1)
    
    def dfs(v):
        visited[v] = True
	for i in graph[v]:
            if not visited[i]:
                dfs(i)
        answer.append(v)
    
    visited = [False] * n
    answer = []
    dfs(1)
    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
