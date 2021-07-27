import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize # 최대치

#입력
V, E = map(int, input().split())
start = int(input())

# 준비물
graph = [[] for _ in range(V+1)]
distances = [INF] * (V+1)
q = []

# 다익스트라
def dijkstra(graph, start):
    # 시작점은 0으로 초기화
    distances[start] = 0
    #첫번째 힙에 추가
    heapq.heappush(q, [distances[start], start])
    while q:
        cur_dist, cur_pos = heapq.heappop(q)

        if distances[cur_pos] < cur_dist:
            continue
        #인접 정점들 방문
        for new_distance, new_destination in graph[cur_pos]:
            distance = cur_dist + new_distance
            # 새로운 누적 거리가 더 작으면 -> 최솟값 갱신
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))
dijkstra(graph, start)

for d in distances[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)