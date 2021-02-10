# list version
graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

# set version
graph2 = {
    '0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}


def DFS_list(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            DFS_list(graph, n, visited)
    return visited

def DFS_set(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for n in graph[node]:
            DFS_set(graph, n, visited)
    return visited




#visited = DFS(graph1, 'A', [])
visited2 = DFS_set(graph2, '0', set())
print(visited2)
