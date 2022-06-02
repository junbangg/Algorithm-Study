from collections import defaultdict
from collections import deque

def solution(n, edge):
    nodes = defaultdict(list)
    for a, b in edge:
        nodes[a].append(b)
        nodes[b].append(a)
    
    maxDistance = 0
    distances = [float('inf') for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    q = deque([1])
    distances[1] = 0
    
    while q:
        current = q.popleft()
        
        for next in nodes[current]:
            if distances[current] + 1 < distances[next]:
                distances[next] = distances[current] + 1
                maxDistance = max(maxDistance, distances[next])
                dp[distances[next]] += 1
                q.append(next)

    return dp[maxDistance]
