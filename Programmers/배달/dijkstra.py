from collections import defaultdict
import heapq
def solution(N, road, K):
    # create map
    map, dp = defaultdict(list), defaultdict(int)
    answer = set()
    for a, b, weight in road:
        map[a].append((weight, b))
        map[b].append((weight, a))
    # weight, node
    q = [(0, 1)]
    while q:
        weight, node = heapq.heappop(q)
        if node not in dp:
            dp[node] = weight
            if dp[node] <= K:
                answer.add(node)
            for nextWeight, nextNode in map[node]:
                heapq.heappush(q, (nextWeight + weight, nextNode))
    print(answer)
    print(dp)
    return len(answer)


N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4
print(solution(N, road, K))

