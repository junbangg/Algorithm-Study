import sys, collections
# def isCycle(cur_node, visited, parent):
#     visited[cur_node] = 1
#     for nxt_node in graph[cur_node]:
#         if not visited[nxt_node]:
#             if isCycle(nxt_node, visited, cur_node):
#                 return True
#         elif parent != nxt_node:
#             return True
#     return False

def isCycle(start, visited):
    q = collections.deque()
    q.append((start, -1))
    visited[start] = 1
    while q:
        cur_node, parent = q.popleft()
        for nxt_node in graph[cur_node]:
            if not visited[nxt_node]:
                visited[nxt_node] = 1
                q.append((nxt_node, cur_node))
            elif parent != nxt_node:
                return True
    return False

input = sys.stdin.readline
N, M = map(int, input().split())
graph = collections.defaultdict(list)
for i in range(1, M+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    visited = [0] * N
    if not visited[a]:
        if isCycle(a, visited):
            print(i)
            exit(0)
    if not visited[b]:
        if isCycle(b, visited):
            print(i)
            exit(0)
print(0)