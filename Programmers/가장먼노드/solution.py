import collections
def solution(n, edge):
    # graph
    graph = collections.defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    # dictionary that holds distance values for each node
    dp = {}
    for node in graph:
        dp[node] = 10
    # visited array set to False
    visited = [False] * n
    # Queue
    q = collections.deque()
    # Add node 1
    q.append(1)
    visited[0] = True
    while q:
        cur = q.popleft()
        for node in graph[cur]:
            if not visited[node-1]:
                # update distance to node
                dp[node] = dp[cur]+ 1
                # check in visited
                visited[node-1] = True
                q.append(node)
    dp_vals = list(dp.values())
    return dp_vals.count(max(dp_vals))

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
