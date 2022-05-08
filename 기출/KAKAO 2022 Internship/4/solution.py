from collections import defaultdict
from copy import deepcopy

def solution(n, paths, gates, summits):
    _map = defaultdict(list)
    for a, b, c in paths:
        _map[a].append([b, c])
        _map[b].append([a, c])

    def dfs(node, cost, destination, visited):
        if node == destination:
            return cost
        for next, nextCost in _map[node]:
            if visited[next]:
                continue
            nextVisited = deepcopy(visited)
            nextVisited[next] = 1
            nextCost = max(cost, nextCost)
            dfs(next, nextCost, destination, nextVisited)
    visited = [0 for _ in range(n+1)]
    answerSummit = 0
    answerCost = float('inf')
    for gate in gates:
        maxCost = 0
        for summit in summits:
            newVisited = deepcopy(visited)
            newVisited[gate] = 1
            cost = dfs(gate, 0, summit, newVisited)
            if cost:
                maxCost = max(cost, maxCost)
            newVisited = deepcopy(visited)
            newVisited[summit] = 1
            cost = dfs(summit, 0, gate, visited)
            if cost:
                maxCost = max(cost, maxCost)
            if maxCost < answerCost:
                answerCost = maxCost
                answerSummit = summit

    return answerSummit, answerCost