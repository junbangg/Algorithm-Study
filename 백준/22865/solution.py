from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N = int(input())
friends = list(map(int, input().split()))
edgeCount = int(input())
graph = defaultdict(list)

for _ in range(edgeCount):
    a, b, weight = map(int, input().split())
    graph[a].append([b, weight])
    graph[b].append([a, weight])

def dijkstra(src):
    distance = [float('inf') for _ in range(len(graph)+1)]
    distance[src] = 0
    q = []
    heapq.heappush(q, (0, src))

    while q:
        _, current = heapq.heappop(q)
        for nextNode, nextWeight in graph[current]:
            if distance[current] + nextWeight < distance[nextNode]:
                distance[nextNode] = distance[current] + nextWeight
                heapq.heappush(q, (distance[nextNode], nextNode))
    return distance

max_size = 0
answer = 0
dist_a = dijkstra(friends[0])
dist_b = dijkstra(friends[1])
dist_c = dijkstra(friends[2])
 
for i in range(1, N+1):
    if max_size < min(dist_a[i], dist_b[i], dist_c[i]):
        max_size = min(dist_a[i], dist_b[i], dist_c[i])
        answer = i
        
print(answer)