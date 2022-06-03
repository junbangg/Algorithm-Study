from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(marker, current):
            for next in cities[current]:
                if visited[next] >= 0:
                    continue
                visited[next] = marker
                dfs(marker, next)
            
        n = len(isConnected)
        cities = defaultdict(list)
        visited = [-1] * n
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    cities[i].append(j)
        for node in range(n):
            dfs(node, node)
            
        return len(set(visited))
