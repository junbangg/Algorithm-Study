from collections import defaultdict
network = set()
def dfs(id, dic):
    if id not in network:
        network.add(id)
        for v in dic[id]:
            dfs(v, dic)
    return
n = int(input())
for _ in range(n):
    i = int(input())
    dic = defaultdict(list)
    for _ in range(i):
        network.clear()
        a, b = input().split(' ')
        dic[a].append(b)
        dic[b].append(a)
        # dfs
        dfs(a, dic)
        print(len(network))