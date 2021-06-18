from collections import defaultdict, deque
def solution(N, road, K):
    map, dp = defaultdict(deque), defaultdict(int)
    q, answer = deque(), set()

    # create map
    for node in road:
        a, b, weight = node
        map[a].append((b, weight))
        map[b].append((a, weight))
    # first node (node, accumulative_weight)
    q.append((1, 0))
    # bfs
    print(map)
    while q:
        cur, cost = q.popleft()
        if dp[cur] == 0:
            dp[cur] = cost
        else:
            dp[cur] = min(dp[cur], cost)
        if dp[cur] <= K:
            answer.add(cur)
        while map[cur]:
            node, weight = map[cur].popleft()
            q.append((node, weight + cost))
    print(dp)
    return len(answer)

N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4
print(solution(N, road, K))