import heapq
from collections import defaultdict

def shortestPath(graph, src, dest):
    h = []
    # keep a track record of vertices with cost
    # heappop will return vertex with minimum cost
    # Since this is a greedy algorithm, SRC -> MIN -> MIN -> Dest
    heapq.heappush(h, (0, src))
    while len(h) != 0:
        currcost, currvtx = heapq.heappop(h)
        if currvtx == dest:
            print("path exists {} to {} with cost{}".format(src, dest, currcost))
            break
        for neight, neighcost in graph[currvtx]:
            heapq.heappush(h, (curcost+neighcost, neigh))

graph = defaultdict(list)
v, e = map(int, input().split())
for i in range(e):
    u, v, w = map(str, input().split())
    graph[u].append((v, int(w)))
src, dest = map(int, input().split())
shortestPath(graph, src, dest)

'''
6 7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
A D
'''
